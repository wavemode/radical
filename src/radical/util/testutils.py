from dataclasses import dataclass
import os
from pathlib import Path

from radical.effect.filesystem.file_reader import FileReader
from radical.unit.compiler.analyzer import Analyzer
from radical.unit.compiler.loader import Loader
from radical.unit.interp.interpreter import Interpreter
from radical.unit.parser.lexer import Lexer
import json

from radical.unit.parser.parser import Parser
from radical.unit.sema.namespace import Namespace


@dataclass(frozen=True)
class CompilerTestCase:
    path: Path
    contents: str
    expected_output: str | None

    def assert_expected_output(self, actual_output: str) -> None:
        if self.expected_output is None:
            raise ValueError("No expected output defined for this test case.")
        if actual_output != self.expected_output:
            raise AssertionError(
                f"Parsed output did not match expected output."
                f"\n\nExpected:\n{self.expected_output}\n\n"
                f"Got:\n{actual_output}"
            )

    def update_expected_output(self, new_output: str) -> None:
        with open(self.path, "r") as f:
            text = f.read()
        test_case_start = text.rfind("(*")
        test_case_end = text.rfind("*)") + 2

        if test_case_start == -1 or test_case_end == -1:
            test_case_start = len(text)
            test_case_end = len(text)

        new_text_parts = [
            text[:test_case_start],
            "(*\n",
            new_output,
            "\n*)",
            text[test_case_end:],
        ]

        # add a newline if the file does not end with one
        if (not new_text_parts[-1]) or (not new_text_parts[-1].endswith("\n")):
            new_text_parts.append("\n")
        new_text = "".join(new_text_parts)

        with open(self.path, "w") as f:
            f.write(new_text)


def collect_test_cases(directory: str) -> list[CompilerTestCase]:
    enabled_files_env = os.environ.get("RAD_TEST_FILES")
    enabled_files: list[str] | None = None
    if enabled_files_env:
        enabled_files = enabled_files_env.split(",")
    result: list[CompilerTestCase] = []
    for root, _, files in os.walk(directory):
        for file in files:
            if not file.endswith(".rad"):
                print("Skipping file:", file)
                continue
            file_path = os.path.join(root, file)
            if enabled_files is not None and file_path not in enabled_files:
                continue
            with open(file_path, "r") as f:
                text = f.read()
            test_case_start = text.rfind("(*")
            test_case_end = text.rfind("*)")
            if test_case_start == -1 or test_case_end == -1:
                expected_output = None
            else:
                expected_output = text[test_case_start + 2 : test_case_end].strip()
            result.append(
                CompilerTestCase(
                    path=Path(file_path),
                    contents=text,
                    expected_output=expected_output,
                )
            )
    return result


def evaluate_lexer_test_case(test_case: CompilerTestCase) -> str:
    try:
        with Lexer(test_case.contents, filename=str(test_case.path)) as lexer:
            formatted = "\n".join(str(token) for token in lexer.read_all())
    except Exception as e:
        if "fail_" not in test_case.path.stem:
            raise
        formatted = f"FAIL({json.dumps(str(e))})"
    else:
        if "fail_" in Path(test_case.path).stem:
            print(f"Test case {test_case.path} was expected to fail but succeeded")
    return formatted


def evaluate_parser_test_case(test_case: CompilerTestCase) -> str:
    try:
        with (
            Lexer(test_case.contents, filename=str(test_case.path)) as lexer,
            Parser(lexer=lexer, filename=str(test_case.path)) as parser,
        ):
            formatted = parser.parse_module().format()
    except Exception as e:
        if "fail_" not in test_case.path.stem:
            raise
        formatted = f"FAIL({json.dumps(str(e))})"
    else:
        if "fail_" in test_case.path.stem:
            print(f"Test case {test_case.path} was expected to fail but succeeded")
    return formatted


def evaluate_sema_test_case(test_case: CompilerTestCase) -> str:
    try:
        with (
            FileReader() as file_reader,
            Loader(file_reader) as loader,
            Namespace() as namespace,
            Interpreter(namespace) as interpreter,
            Analyzer(namespace, loader, interpreter) as analyzer,
        ):
            module_id = analyzer.load_module(
                str(test_case.path).replace("/", ".").removesuffix(".rad")
            )
            expected_output = str(
                list(namespace.type_bindings(module_id))
                + list(namespace.bindings(module_id))
            )
    except Exception as e:
        if "Fail" not in test_case.path.stem:
            raise
        expected_output = f"FAIL({json.dumps(str(e))})"
    else:
        if "Fail" in test_case.path.stem:
            print(f"Test case {test_case.path} was expected to fail but succeeded")
    return expected_output
