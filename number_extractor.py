import fileinput
import re

# A regular expression pattern to attempt to extract things that look like a number,
# but might not be valid integers.
FLEXIBLE_NUMBER_REGEX_PATTERN = r"[\d#][\d\s,#]*"


class NumberExtractor:
    encoding: str
    regex: re.Pattern = re.compile(FLEXIBLE_NUMBER_REGEX_PATTERN)

    def __init__(self, encoding: str = "utf-8") -> None:
        self.encoding = encoding

    def extract_numbers(self):
        for line in fileinput.input(encoding=self.encoding):
            line = line.strip()
            if line:
                yield from self.extract_numbers_from_string(line)

    def extract_numbers_from_string(self, text: str) -> list[str]:
        try:
            return [m.strip() for m in self.regex.findall(text)]
        except re.error:
            return []
