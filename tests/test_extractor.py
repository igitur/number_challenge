import pytest

from number_extractor import NumberExtractor


class TestExtractor:
    @pytest.mark.parametrize(
        "line, expected_numbers",
        [
            ("The pump is 536 deep underground.", ["536"]),
            ("We processed 9121 records.", ["9121"]),
            ("Variables reported as having a missing type #65678.", ["#65678"]),
            ("Interactive and printable 10022 ZIP code.", ["10022"]),
            ("The database has 66723107008 records.", ["66723107008"]),
            ("I received 23 456,9 KGs.number invalid", ["23 456,9"]),
            ("This is a string with 49 characters and 10 words.", ["49", "10"]),
            ("This is a string with 7 words.", ["7"]),
            ("", []),  # Empty line
            ("No numbers here.", []),  # Line with no numbers
            ("Number at start 123 and end 456.", ["123", "456"]),
        ],
    )
    def test_extraction(self, line, expected_numbers):
        extractor = NumberExtractor()
        results = list(extractor.extract_numbers_from_string(line))
        assert results == expected_numbers
