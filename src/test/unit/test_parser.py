from unittest import TestCase


from radical.util.testutils import collect_test_cases, evaluate_parser_test_case


class TestParser(TestCase):
    maxDiff = None

    def test_all_cases(self):
        test_cases = collect_test_cases("test_cases/parser")
        for test_case in test_cases:
            with self.subTest(test_case.path):
                expected_output = evaluate_parser_test_case(test_case)
                self.assertEqual(
                    test_case.expected_output,
                    expected_output,
                )
