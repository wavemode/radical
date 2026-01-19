#!/usr/bin/env python3

from radical.unit.parser.tokenizer import Tokenizer

from radical.util.testutils import collect_test_cases


def _tokenizer_from_text(text: str, filename: str) -> Tokenizer:
    return Tokenizer(text, filename=filename)


def fix_tokenizer_tests():
    for test_case in collect_test_cases("test_cases/tokenizer"):
        tokenizer = _tokenizer_from_text(
            test_case.contents, filename=test_case.path
        )
        formatted = "\n".join(
            str(token) for token in tokenizer.tokens()
        )
        test_case.update_expected_output(formatted)


if __name__ == "__main__":
    fix_tokenizer_tests()
    # run it again in case we messed up line/column positions
    fix_tokenizer_tests()
