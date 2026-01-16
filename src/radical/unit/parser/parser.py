from typing import NoReturn, cast
from radical.data.parser.ast import (
    VariableBindingStatementNode,
    ModuleNode,
    MultiLineStringLiteralNode,
    RawMultiLineStringLiteralNode,
    RawStringLiteralNode,
    StringLiteralNode,
    SymbolNode,
    TopLevelDeclarationNodeType,
    ValueExpressionNodeType,
    IntegerLiteralNode,
    FloatLiteralNode,
    SciFloatLiteralNode,
    UnaryOperator,
    BinaryOperator,
    precedence_of_binary_op,
    precendence_of_unary_op,
    associativity_of_binary_op,
    associativity_of_unary_op,
    OperatorAssociativity,
    UnaryOperationNode,
    BinaryOperationNode,
    ParenthesizedExpressionNode,
    SetLiteralNode,
    SetComprehensionNode,
    MapLiteralNode,
    MapComprehensionNode,
    IndexAccessNode,
    SliceAccessNode,
    AttributeAccessNode,
    FunctionCallArgumentNode,
    FunctionCallNode,
    ListLiteralNode,
    TupleLiteralNode,
    ListComprehensionNode,
    ComprehensionBindingNode,
    ComprehensionGuardNode,
    MapEntryNode,
    TreeEntryNode,
    TreeLiteralNode,
    TreeComprehensionNode,
    IfThenElseNode,
    SpreadOperationNode,
    CollectionElementNodeType,
)
from radical.data.parser.errors import ParseError
from radical.data.parser.position import Position
from radical.unit.parser.char_stream import CharStream
from radical.util.core.unit import Unit


class Parser(Unit):
    _char_stream: CharStream
    _filename: str

    def __init__(self, char_stream: CharStream, filename: str) -> None:
        super().__init__()
        self._char_stream = self.add_child(char_stream)
        self._filename = filename
        self._seen_non_whitespace = False
        self._indent_level = 0

    def parse_module(self) -> ModuleNode:
        position = self._position()
        top_level_nodes: list[TopLevelDeclarationNodeType] = []
        self.skip_whitespace()
        while not self.at_end():
            if not self._indent_level == 0:
                self._raise_parse_error("Unexpected indentation at top-level")
            top_level_nodes.append(self.parse_top_level_declaration())
            self.skip_whitespace()
        return ModuleNode(
            position=position,
            top_level_nodes=top_level_nodes,
        )

    def parse_top_level_declaration(self) -> TopLevelDeclarationNodeType:
        if self.check_symbol():
            return self.parse_variable_binding()
        else:
            self._raise_parse_error("Expected a top-level declaration")

    def parse_variable_binding(self) -> VariableBindingStatementNode:
        # TODO: support type annotation
        start_position = self._position()
        name_node = self.parse_symbol()
        self.skip_non_breaking_whitespace()
        self.parse_specific_charachters("=")
        self.skip_whitespace()
        value_node = self.parse_value()
        return VariableBindingStatementNode(
            position=start_position,
            name=name_node,
            value=value_node,
            type=None,
        )

    def parse_value(self, min_precedence: int = 0) -> ValueExpressionNodeType:
        position_before_lhs = self._position()
        lhs: ValueExpressionNodeType | None = None
        if not self.check_unary_operator():
            lhs = self.parse_single_value_expression()
            self.skip_non_breaking_whitespace()

        while not self.at_end():
            position_before_op = self._position()
            op: BinaryOperator | UnaryOperator | None = None
            if lhs is None:
                op = self.parse_unary_operator()
            elif self.check_binary_operator():
                op = self.parse_binary_operator()

            if op is None:
                break

            precedence: int
            associativity: OperatorAssociativity

            if isinstance(op, BinaryOperator):
                precedence = precedence_of_binary_op(op)
                associativity = associativity_of_binary_op(op)
                if precedence < min_precedence:
                    self._reset_position(position_before_op)
                    break
            else:
                precedence = precendence_of_unary_op(op)
                associativity = associativity_of_unary_op(op)

            self.skip_whitespace()
            rhs = self.parse_value(
                min_precedence=(
                    # Adding 1 makes it so that another operation to the right with the same precedence
                    # level as the current operator will not be included in the rhs expression (due to
                    # the min_precedence now being 1 higher than the current operator's precedence).
                    # Thus causing left associativity (e.g. a - b - c  parsed as (a - b) - c).
                    precedence + 1
                    if associativity == OperatorAssociativity.LEFT
                    else precedence
                )
            )
            if isinstance(op, UnaryOperator):
                lhs = UnaryOperationNode(
                    operator=op, operand=rhs, position=position_before_op
                )
            else:
                assert lhs is not None
                lhs = BinaryOperationNode(
                    left=lhs,
                    operator=op,
                    right=rhs,
                    position=position_before_lhs,
                )
            self.skip_non_breaking_whitespace()

        assert lhs is not None
        return lhs

    def parse_single_value_expression(self) -> ValueExpressionNodeType:
        value: ValueExpressionNodeType
        if self.check_parenthesized_expression():
            value = self.parse_parenthesized_expression()
        elif self.check_if_then_else():
            value = self.parse_if_then_else()
        elif self.check_list_literal():
            value = self.parse_list_literal()
        elif self.check_set_or_map_or_tree_literal():
            value = self.parse_set_or_map_or_tree_literal()
        elif self.check_raw_multi_line_string_literal():
            value = self.parse_raw_multi_line_string_literal()
        elif self.check_raw_string_literal():
            value = self.parse_raw_string_literal()
        elif self.check_multi_line_string_literal():
            value = self.parse_multi_line_string_literal()
        elif self.check_string_literal():
            value = self.parse_string_literal()
        elif self.check_number_literal():
            value = self.parse_number_literal()
        elif self.check_symbol():
            value = self.parse_symbol()
        else:
            self._raise_parse_error("Expected a value")

        while not self.at_end():
            if self.check_specific_charachters("["):
                value = self.parse_index_or_slice_access(value)
            elif self.check_specific_charachters("."):
                value = self.parse_attribute_access(value)
            elif self.check_specific_charachters("("):
                value = self.parse_function_call(value)
            else:
                break

        return value

    def parse_function_call(
        self, function: ValueExpressionNodeType
    ) -> FunctionCallNode:
        start_position = function.position
        self.parse_specific_charachters("(")
        self.skip_whitespace()

        arguments: list[FunctionCallArgumentNode] = []

        while not self.check_specific_charachters(")"):
            arguments.append(self.parse_function_call_argument())
            self.skip_whitespace()
            if self.check_specific_charachters(","):
                self._read()
            self.skip_whitespace()

        self.parse_specific_charachters(")")
        return FunctionCallNode(
            position=start_position,
            function=function,
            arguments=arguments,
        )

    def parse_function_call_argument(self) -> FunctionCallArgumentNode:
        start_position = self._position()
        name: SymbolNode | None = None
        value: ValueExpressionNodeType
        if self.check_symbol():
            name = self.parse_symbol()
            self.skip_whitespace()
            if self.check_specific_charachters("="):
                self.parse_specific_charachters("=")
                self.skip_whitespace()
                value = self.parse_value()
            else:
                self._reset_position(start_position)
                value = self.parse_value()
                name = None
        else:
            value = self.parse_value()

        return FunctionCallArgumentNode(
            position=start_position,
            name=name,
            value=value,
        )

    def parse_attribute_access(
        self, object: ValueExpressionNodeType
    ) -> AttributeAccessNode:
        start_position = object.position
        self.parse_specific_charachters(".")
        self.skip_whitespace()
        attribute = self.parse_symbol()
        return AttributeAccessNode(
            position=start_position,
            object=object,
            attribute=attribute,
        )

    def parse_index_or_slice_access(
        self, collection: ValueExpressionNodeType
    ) -> SliceAccessNode | IndexAccessNode:
        start_position = collection.position
        self.parse_specific_charachters("[")
        self.skip_whitespace()

        is_slice = False
        slice_start: ValueExpressionNodeType | None = None
        slice_end: ValueExpressionNodeType | None = None

        if not self.check_specific_charachters(":"):
            slice_start = self.parse_value()
            self.skip_whitespace()

        if self.check_specific_charachters(":"):
            is_slice = True
            self._read()
            self.skip_whitespace()
            if not self.check_specific_charachters("]"):
                slice_end = self.parse_value()
                self.skip_whitespace()

        self.parse_specific_charachters("]")
        if is_slice:
            return SliceAccessNode(
                position=start_position,
                collection=collection,
                start=slice_start,
                end=slice_end,
            )
        else:
            assert slice_start is not None
            return IndexAccessNode(
                position=start_position,
                collection=collection,
                index=slice_start,
            )

    def check_if_then_else(self) -> bool:
        return self.check_word("if")

    def parse_if_then_else(self) -> IfThenElseNode:
        start_position = self._position()
        self.parse_word("if")
        self.skip_whitespace()
        condition = self.parse_value()
        self.skip_whitespace()
        self.parse_word("then")
        self.skip_whitespace()
        then_branch = self.parse_value()
        self.skip_whitespace()
        self.parse_word("else")
        self.skip_whitespace()
        else_branch = self.parse_value()
        return IfThenElseNode(
            position=start_position,
            condition=condition,
            then_branch=then_branch,
            else_branch=else_branch,
        )

    def check_comprehension_clause(self) -> bool:
        return self.check_any_word(["for", "if"])

    def parse_comprehension_clauses(
        self,
    ) -> list[ComprehensionGuardNode | ComprehensionBindingNode]:
        clauses: list[ComprehensionGuardNode | ComprehensionBindingNode] = []
        while True:
            if self.check_word("for"):
                start_position = self._position()
                self._read(3)
                self.skip_whitespace()
                variables: list[SymbolNode] = []
                variables.append(self.parse_symbol())
                self.skip_whitespace()
                while self.check_specific_charachters(","):
                    self._read()
                    self.skip_whitespace()
                    variables.append(self.parse_symbol())
                    self.skip_whitespace()
                self.parse_word("in")
                self.skip_whitespace()
                iterable = self.parse_value()
                self.skip_whitespace()
                clauses.append(
                    ComprehensionBindingNode(
                        position=start_position,
                        variables=variables,
                        iterable=iterable,
                    )
                )
            elif self.check_word("if"):
                start_position = self._position()
                self._read(2)
                self.skip_whitespace()
                condition = self.parse_value()
                self.skip_whitespace()
                clauses.append(
                    ComprehensionGuardNode(
                        position=start_position,
                        condition=condition,
                    )
                )
            else:
                break
        return clauses

    def check_spread_operation(self) -> bool:
        return self.check_specific_charachters("...")

    def parse_spread_operation(self) -> SpreadOperationNode:
        start_position = self._position()
        self.parse_specific_charachters("...")
        self.skip_whitespace()
        collection = self.parse_value()
        return SpreadOperationNode(
            position=start_position,
            collection=collection,
        )

    def check_list_literal(self) -> bool:
        return self.check_specific_charachters("[")

    def parse_list_literal(self) -> ListLiteralNode | ListComprehensionNode:
        start_position = self._position()
        self.parse_specific_charachters("[")
        self.skip_whitespace()

        elements: list[ValueExpressionNodeType | SpreadOperationNode] = []
        while not self.check_specific_charachters("]"):
            if self.check_comprehension_clause():
                if len(elements) != 1:
                    self._raise_parse_error(
                        "List comprehension must have exactly one element expression",
                        position=start_position,
                    )
                elif isinstance(elements[0], SpreadOperationNode):
                    self._raise_parse_error(
                        "List comprehension element cannot be a spread operation",
                        position=start_position,
                    )
                clauses = self.parse_comprehension_clauses()
                self.skip_whitespace()
                self.parse_specific_charachters("]")

                # satisfy typechecker
                assert not isinstance(elements[0], SpreadOperationNode)

                return ListComprehensionNode(
                    position=start_position,
                    element=elements[0],
                    clauses=clauses,
                )

            elements.append(
                self.parse_spread_operation()
                if self.check_spread_operation()
                else self.parse_value()
            )
            self.skip_non_breaking_whitespace()
            if self.check_specific_charachters(","):
                self._read()
                self.skip_whitespace()
            elif self.check_specific_charachters("\n"):
                self.skip_whitespace()
                if self.check_specific_charachters(","):
                    self._read()
                    self.skip_whitespace()
            elif self.check_specific_charachters("]"):
                break
            elif not self.check_comprehension_clause():
                self._raise_parse_error(
                    "Expected either ',' or newline between collection elements",
                )

        self.parse_specific_charachters("]")
        return ListLiteralNode(
            position=start_position,
            elements=elements,
        )

    def check_set_or_map_or_tree_literal(self) -> bool:
        return self.check_specific_charachters("{")

    def parse_set_or_map_or_tree_literal(
        self,
    ) -> (
        SetLiteralNode
        | MapLiteralNode
        | SetComprehensionNode
        | MapComprehensionNode
        | TreeLiteralNode
        | TreeComprehensionNode
    ):
        start_position = self._position()
        self.parse_specific_charachters("{")
        self.skip_whitespace()

        has_tree_entries = False
        has_set_entries = False
        has_map_entries = False
        elements: list[CollectionElementNodeType] = []

        while not self.check_specific_charachters("}"):
            if self.check_comprehension_clause():
                if len(elements) != 1:
                    self._raise_parse_error(
                        "Comprehension must have exactly one key/value or element expression",
                        position=start_position,
                    )
                if isinstance(elements[0], SpreadOperationNode):
                    self._raise_parse_error(
                        "Comprehension element cannot be a spread operation",
                        position=start_position,
                    )

                clauses = self.parse_comprehension_clauses()
                self.skip_whitespace()
                self.parse_specific_charachters("}")

                if isinstance(elements[0], MapEntryNode):
                    return MapComprehensionNode(
                        position=start_position,
                        entry=elements[0],
                        clauses=clauses,
                    )
                elif isinstance(elements[0], TreeEntryNode):
                    return TreeComprehensionNode(
                        position=start_position,
                        entry=elements[0],
                        clauses=clauses,
                    )
                else:
                    # satisfy typechecker
                    assert not isinstance(elements[0], SpreadOperationNode)

                    return SetComprehensionNode(
                        position=start_position,
                        element=elements[0],
                        clauses=clauses,
                    )

            if self.check_spread_operation():
                elements.append(self.parse_spread_operation())
            else:
                key_or_element = self.parse_value()
                expression_key = False
                self.skip_non_breaking_whitespace()
                if self.check_specific_charachters("="):
                    if isinstance(key_or_element, ListLiteralNode):
                        if not len(key_or_element.elements) == 1:
                            self._raise_parse_error(
                                "Map key must be a single value",
                                position=key_or_element.position,
                            )
                        key_or_element = key_or_element.elements[0]
                        expression_key = True
                    elif not isinstance(key_or_element, SymbolNode):
                        self._raise_parse_error(
                            "Map key must be a symbol",
                            position=key_or_element.position,
                        )

                    self._read()
                    self.skip_whitespace()
                    value = self.parse_value()

                    has_map_entries = True
                    if has_tree_entries:
                        self._raise_parse_error(
                            "Cannot mix map entries and tree entries in the same literal",
                            position=start_position,
                        )
                    elif has_set_entries:
                        self._raise_parse_error(
                            "Cannot mix map entries and set elements in the same literal",
                            position=start_position,
                        )

                    # satisfy typechecker
                    assert not isinstance(key_or_element, SpreadOperationNode)

                    elements.append(
                        MapEntryNode(
                            position=key_or_element.position,
                            key=key_or_element,
                            value=value,
                            expression_key=expression_key,
                        )
                    )
                elif (
                    not self.check_any_sequence([",", "\n", "}"])
                    and not self.check_comprehension_clause()
                ):
                    if isinstance(key_or_element, ListLiteralNode):
                        if not len(key_or_element.elements) == 1:
                            self._raise_parse_error(
                                "Tree key must be a single value",
                                position=key_or_element.position,
                            )
                        key_or_element = key_or_element.elements[0]
                        expression_key = True
                    elif not isinstance(key_or_element, SymbolNode):
                        self._raise_parse_error(
                            "Tree key must be a symbol",
                            position=key_or_element.position,
                        )

                    value = self.parse_value()

                    has_tree_entries = True
                    if has_map_entries:
                        self._raise_parse_error(
                            "Cannot mix tree entries and map entries in the same literal",
                            position=start_position,
                        )
                    elif has_set_entries:
                        self._raise_parse_error(
                            "Cannot mix tree entries and set elements in the same literal",
                            position=start_position,
                        )

                    # satisfy typechecker
                    assert not isinstance(key_or_element, SpreadOperationNode)

                    elements.append(
                        TreeEntryNode(
                            position=key_or_element.position,
                            key=key_or_element,
                            value=value,
                            expression_key=expression_key,
                        )
                    )
                else:
                    has_set_entries = True
                    if has_map_entries or has_tree_entries:
                        self._raise_parse_error(
                            "Map or tree literals must have key/value pairs",
                            position=start_position,
                        )
                    elements.append(key_or_element)

            if self.check_specific_charachters(","):
                self._read()
                self.skip_whitespace()
            elif self.check_specific_charachters("\n"):
                self.skip_whitespace()
                if self.check_specific_charachters(","):
                    self._read()
                    self.skip_whitespace()
            elif self.check_specific_charachters("}"):
                break
            elif not self.check_comprehension_clause():
                self._raise_parse_error(
                    "Expected either ',' or newline between collection elements"
                )

        self.parse_specific_charachters("}")

        if has_map_entries or (not has_tree_entries and not has_set_entries):
            return MapLiteralNode(
                position=start_position,
                entries=cast(list[MapEntryNode | SpreadOperationNode], elements),
            )
        elif has_tree_entries:
            return TreeLiteralNode(
                position=start_position,
                entries=cast(list[TreeEntryNode | SpreadOperationNode], elements),
            )
        else:
            return SetLiteralNode(
                position=start_position,
                elements=cast(
                    list[ValueExpressionNodeType | SpreadOperationNode], elements
                ),
            )

    def check_parenthesized_expression(self) -> bool:
        return self.check_specific_charachters("(")

    def parse_parenthesized_expression(
        self,
    ) -> ParenthesizedExpressionNode | TupleLiteralNode:
        start_position = self._position()
        self.parse_specific_charachters("(")
        self.skip_whitespace()
        expression = self.parse_value()
        self.skip_whitespace()

        if self.check_specific_charachters(","):
            self._read()
            self.skip_whitespace()

            elements: list[ValueExpressionNodeType] = [expression]
            while not self.check_specific_charachters(")"):
                elements.append(self.parse_value())
                self.skip_whitespace()
                if self.check_specific_charachters(","):
                    self._read()
                    self.skip_whitespace()
            self.parse_specific_charachters(")")
            return TupleLiteralNode(
                position=start_position,
                elements=elements,
            )

        self.parse_specific_charachters(")")
        return ParenthesizedExpressionNode(
            position=start_position,
            expression=expression,
        )

    def check_binary_operator(self) -> bool:
        return self.check_any_sequence(
            [
                op.value
                for op in BinaryOperator
                if op not in (BinaryOperator.AND, BinaryOperator.OR)
            ]
        ) or self.check_any_word(["and", "or"])

    def parse_binary_operator(self) -> BinaryOperator:
        if self.check_word("and"):
            self._read(3)
            return BinaryOperator.AND
        elif self.check_word("or"):
            self._read(2)
            return BinaryOperator.OR
        else:
            operator_str = self.parse_any_sequence(
                [
                    op.value
                    for op in BinaryOperator
                    if op not in (BinaryOperator.AND, BinaryOperator.OR)
                ]
            )
            return BinaryOperator(operator_str)

    def check_unary_operator(self) -> bool:
        return self.check_any_sequence(["+", "-"]) or self.check_word("not")

    def parse_unary_operator(self) -> UnaryOperator:
        if self.check_word("not"):
            self._read(3)
            return UnaryOperator.NOT
        else:
            return UnaryOperator(self._read())

    def check_number_literal(self) -> bool:
        return self._peek().isdigit()

    def parse_number_literal(
        self,
    ) -> SciFloatLiteralNode | FloatLiteralNode | IntegerLiteralNode:
        position = self._position()

        integer_chars = self.parse_numeral_sequence()
        fractional_chars: list[str] | None = None
        e: str | None = None
        exponent_chars: list[str] | None = None
        exponent_sign: str | None = None

        if self.check_specific_charachters("."):
            self._read()
            fractional_chars = self.parse_numeral_sequence()

        if self.check_any_sequence(["e", "E"]):
            e = self._read()
            if self._peek() in ("+", "-"):
                exponent_sign = self._read()
            exponent_chars = self.parse_numeral_sequence()

        if exponent_chars is not None:
            parts: list[str] = [*integer_chars]
            if fractional_chars is not None:
                parts.append(".")
                parts.extend(fractional_chars)
            assert e is not None
            parts.append(e)
            parts.append(exponent_sign or "")
            parts.extend(exponent_chars)

            return SciFloatLiteralNode(
                position=position,
                value="".join(parts),
            )

        if fractional_chars is not None:
            value_parts: list[str] = [
                *integer_chars,
                ".",
                *fractional_chars,
            ]
            return FloatLiteralNode(
                position=position,
                value="".join(value_parts),
            )

        value = "".join(integer_chars)
        return IntegerLiteralNode(
            position=self._position(),
            value=value,
        )

    def parse_numeral_sequence(self) -> list[str]:
        numeral_chars: list[str] = []
        while True:
            char = self._peek()
            if char.isdigit():
                numeral_chars.append(self._read())
            else:
                break
        if not numeral_chars:
            self._raise_parse_error("Expected numeral sequence")
        return numeral_chars

    def check_symbol(self) -> bool:
        # TODO: support backtick-quoted symbols
        char = self._peek()
        return char.isalpha() or char == "_"

    def parse_symbol(self) -> SymbolNode:
        start_position = self._position()
        name_chars: list[str] = []
        char = self._peek()
        if char.isalpha() or char == "_":
            name_chars.append(self._read())
        else:
            self._raise_parse_error("Expected symbol", position=start_position)
        while True:
            if self._peek().isalnum() or self._peek() == "_":
                name_chars.append(self._read())
            else:
                break
        return SymbolNode(
            position=start_position,
            name="".join(name_chars),
        )

    def check_string_literal(self) -> bool:
        return self.check_specific_charachters('"')

    def parse_string_literal(self) -> StringLiteralNode:
        start_position = self._position()
        self.parse_specific_charachters('"')
        value_chars: list[str] = []
        while not self.at_end() and not self._peek() == "\n":
            if self.check_specific_charachters('"'):
                self._read()
                return StringLiteralNode(
                    position=start_position,
                    value="".join(value_chars),
                )
            elif self.check_specific_charachters("\\"):
                value_chars.append(self.parse_string_literal_escape_sequence())
            else:
                value_chars.append(self._read())
        self._raise_parse_error("Unterminated string literal", position=start_position)

    def check_multi_line_string_literal(self) -> bool:
        return self.check_specific_charachters('"""')

    def parse_multi_line_string_literal(self) -> MultiLineStringLiteralNode:
        start_position = self._position()
        self.parse_specific_charachters('"""')
        value_chars: list[str] = []
        while not self.at_end():
            if self.check_specific_charachters('"""'):
                self._read(3)
                return MultiLineStringLiteralNode(
                    position=start_position,
                    value="".join(value_chars),
                )
            elif self.check_specific_charachters("\\"):
                value_chars.append(self.parse_string_literal_escape_sequence())
            else:
                value_chars.append(self._read())
        self._raise_parse_error(
            "Unterminated multi-line string literal", position=start_position
        )

    def check_raw_string_literal(self) -> bool:
        return self.check_specific_charachters('r"')

    def parse_raw_string_literal(self) -> RawStringLiteralNode:
        start_position = self._position()
        self.parse_specific_charachters('r"')
        value_chars: list[str] = []
        while not self.at_end() and not self._peek() == "\n":
            if self.check_specific_charachters('"'):
                self._read()
                return RawStringLiteralNode(
                    position=start_position,
                    value="".join(value_chars),
                )
            elif self.check_specific_charachters('""'):
                self._read(2)
                value_chars.append('"')
            else:
                value_chars.append(self._read())
        self._raise_parse_error(
            "Unterminated raw string literal", position=start_position
        )

    def check_raw_multi_line_string_literal(self) -> bool:
        return self.check_specific_charachters('r"""')

    def parse_raw_multi_line_string_literal(self) -> RawMultiLineStringLiteralNode:
        start_position = self._position()
        self.parse_specific_charachters('r"""')
        value_chars: list[str] = []
        while not self.at_end():
            if self.check_specific_charachters('"""'):
                self._read(3)
                return RawMultiLineStringLiteralNode(
                    position=start_position,
                    value="".join(value_chars),
                )
            elif self.check_specific_charachters('""'):
                self._read(2)
                value_chars.append('"')
            else:
                value_chars.append(self._read())
        self._raise_parse_error(
            "Unterminated raw multi-line string literal", position=start_position
        )

    STRING_LITERAL_ESCAPE_SEQUENCES = {
        "n": "\n",
        "r": "\r",
        "t": "\t",
        "\\": "\\",
        '"': '"',
    }

    def parse_string_literal_escape_sequence(self) -> str:
        self.parse_specific_charachters("\\")
        escape_char = self._read()
        if escape_char in self.STRING_LITERAL_ESCAPE_SEQUENCES:
            return self.STRING_LITERAL_ESCAPE_SEQUENCES[escape_char]
        else:
            self._raise_parse_error(
                f"Unknown escape sequence '\\{escape_char}' in string literal"
            )

    def check_single_line_comment(self) -> bool:
        return self.check_specific_charachters("--")

    def skip_single_line_comment(self) -> None:
        self.parse_specific_charachters("--")
        while not self.at_end() and self._peek() != "\n":
            self._read()

    def check_multi_line_comment(self) -> bool:
        return self.check_specific_charachters("(*")

    def skip_multi_line_comment(self) -> None:
        position = self._position()
        self.parse_specific_charachters("(*")
        level = 1
        while not self.at_end():
            if self.check_specific_charachters("(*"):
                level += 1
                self._read(2)
            elif self.check_specific_charachters("*)"):
                level -= 1
                self._read(2)
                if level == 0:
                    return
            else:
                self._read()
        self._raise_parse_error(
            "Unterminated multi-line comment",
            position=position,
        )

    def skip_non_breaking_whitespace(self) -> None:
        self.skip_chars({" ", "\t", "\r"})

    def skip_whitespace(self) -> None:
        self.skip_chars({" ", "\t", "\r", "\n"})

    def skip_chars(self, chars: set[str]) -> None:
        while not self.at_end():
            if self.check_single_line_comment():
                self.skip_single_line_comment()
            elif self.check_multi_line_comment():
                self.skip_multi_line_comment()
            else:
                char = self._peek()
                if char in chars:
                    self._read()
                else:
                    break

    def check_any_sequence(self, expected: list[str]) -> bool:
        position = self._position()
        longest = max(len(seq) for seq in expected)
        chars: list[str] = []
        index = 0
        while not self.at_end() and index < longest:
            chars.append(self._read())
            index += 1
        word = "".join(chars)
        self._reset_position(position)
        return any(word.startswith(seq) for seq in expected)

    def parse_any_sequence(self, expected: list[str]) -> str:
        position = self._position()
        longest = max(len(seq) for seq in expected)
        chars: list[str] = []
        index = 0
        while not self.at_end() and index < longest:
            chars.append(self._read())
            index += 1
        word = "".join(chars)
        self._reset_position(position)
        result = max(
            (seq for seq in expected if word.startswith(seq)),
            key=lambda s: len(s),
        )
        self._read(len(result))
        return result

    def check_any_word(self, expected: list[str]) -> bool:
        for word in expected:
            if self.check_word(word):
                return True
        return False

    def parse_word(self, expected: str) -> str:
        if self.check_word(expected):
            self._read(len(expected))
            return expected
        self._raise_parse_error(f"Expected '{expected}'")

    def parse_any_word(self, expected: list[str]) -> str:
        for word in expected:
            if self.check_word(word):
                self._read(len(word))
                return word
        self._raise_parse_error(f"Expected one of: {', '.join(expected)}")

    def check_word(self, expected: str) -> bool:
        position = self._position()
        matching = True
        index = 0
        while not self.at_end():
            if index == len(expected):
                break
            if self._read() != expected[index]:
                matching = False
                break
            index += 1
        at_end = self.at_end()
        if at_end:
            next_char = ""
        else:
            next_char = self._peek()
        self._reset_position(position)
        return matching and (at_end or not (next_char.isalnum() or next_char == "_"))

    def check_specific_charachters(self, expected: str) -> bool:
        return self._peek(len(expected)) == expected

    def parse_specific_charachters(self, expected: str) -> None:
        actual = self._read(len(expected))
        if actual != expected:
            self._raise_parse_error(f"Expected '{expected}', got '{actual}'")

    def at_end(self) -> bool:
        return self._char_stream.at_end()

    def _peek(self, n: int = 1) -> str:
        if n == 1:
            return "" if self.at_end() else self._char_stream.peek_char()

        position = self._char_stream.get_position()
        chars: list[str] = []
        for _ in range(n):
            if self.at_end():
                break
            chars.append(self._read())
        self._char_stream.reset_position(position)
        return "".join(chars)

    def _read(self, n: int = 1) -> str:
        result = self._peek(n)
        for _ in range(n):
            char = self._char_stream.read_char()
            if char == "\n":
                self._seen_non_whitespace = False
                self._indent_level = 0
            elif char in (" ", "\t"):
                if not self._seen_non_whitespace:
                    self._indent_level += 1
            else:
                self._seen_non_whitespace = True
        return result

    def _position(self) -> Position:
        return self._char_stream.get_position()

    def _reset_position(self, position: Position) -> None:
        self._char_stream.reset_position(position)

    def _raise_parse_error(
        self, message: str, position: Position | None = None
    ) -> NoReturn:
        raise ParseError(
            message,
            position=position or self._position(),
            filename=self._filename,
        )
