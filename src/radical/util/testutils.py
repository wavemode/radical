from dataclasses import dataclass
import os


@dataclass(frozen=True)
class CompilerTestCase:
    path: str
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

        if new_text != text:
            print(f"Updating {self.path}")
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
                    path=file_path,
                    contents=text,
                    expected_output=expected_output,
                )
            )
    return result
