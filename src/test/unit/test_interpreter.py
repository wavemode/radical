from unittest import TestCase

from radical.effect.filesystem.file_reader import FileReader
from radical.unit.compiler.analyzer import Analyzer
from radical.unit.compiler.loader import Loader
from radical.unit.sema.namespace import Namespace
from radical.unit.interp.interpreter import Interpreter


from radical.util.testutils import collect_test_cases


class TestInterpreter(TestCase):
    maxDiff = None

    def setUp(self) -> None:
        self.namespace = Namespace()
        self.interpreter = Interpreter()
        self.file_reader = FileReader()
        self.loader = Loader(self.file_reader)
        self.analyzer = Analyzer(
            namespace=self.namespace,
            loader=self.loader,
            interpreter=self.interpreter,
        )

    def test_all_cases(self):
        test_cases = collect_test_cases("test_cases/interp")
        for test_case in test_cases:
            with self.subTest(test_case.path):
                # TODO: interpreter test cases
                pass
