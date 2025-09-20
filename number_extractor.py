import fileinput
import re

# A regular expression pattern to attempt to extract things that look like a number,
# but might not be valid integers.
FLEXIBLE_NUMBER_REGEX_PATTERN = r"[\d#][\d\s,#]*"


class NumberExtractor:
    """
    Extracts potential number strings from text streams or strings.

    This class uses a flexible regular expression to find sequences that look
    like numbers, including those with spaces, commas, or hash symbols.
    """

    encoding: str
    regex: re.Pattern = re.compile(FLEXIBLE_NUMBER_REGEX_PATTERN)

    def __init__(self, encoding: str = "utf-8") -> None:
        """
        Initializes the NumberExtractor.

        Args:
            encoding: The text encoding to use when reading from fileinput (stdin/files).
                      Defaults to "utf-8".
        """
        self.encoding = encoding

    def extract_numbers(self):
        """
        Reads from standard input or files and yields extracted number strings.

        Uses `fileinput` to iterate over lines from `sys.argv[1:]` or `sys.stdin`
        if no arguments are provided.

        Yields:
            A string for each potential number found in the input stream.
        """
        for line in fileinput.input(encoding=self.encoding):
            line = line.strip()
            if line:
                yield from self.extract_numbers_from_string(line)

    def extract_numbers_from_string(self, text: str) -> list[str]:
        """
        Extracts all potential number strings from a single line of text.

        Args:
            text: The string to search for numbers.

        Returns:
            A list of strings, where each string is a potential number.
        """
        try:
            return [m.strip() for m in self.regex.findall(text)]
        except re.error:
            return []
