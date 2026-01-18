#!/usr/bin/env python3

from typing import cast
from radical.unit.parser.token_stream import TokenStream
from radical.data.parser.token import Token

from radical.util.testutils import collect_test_cases


def _token_stream_from_text(text: str, filename: str) -> TokenStream:
    return TokenStream(text, filename=filename)


def fix_tokenizer_tests():
    for test_case in collect_test_cases("test_cases/tokenizer"):
        token_stream = _token_stream_from_text(
            test_case.contents, filename=test_case.path
        )
        formatted = "\n".join(
            str(token) for token in cast(list[Token], getattr(token_stream, "_tokens"))
        )
        test_case.update_expected_output(formatted)


if __name__ == "__main__":
    fix_tokenizer_tests()
    # run it again in case we messed up line/column positions
    fix_tokenizer_tests()
