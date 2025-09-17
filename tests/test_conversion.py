import pytest

from wordifyer import number_to_words


class TestConversion:
    @pytest.mark.parametrize(
        "number, expected",
        [
            # Simple cases (powers of 10)
            (0, "zero"),
            (10**2, "one hundred"),
            (10**3, "one thousand"),
            (10**6, "one million"),
            (10**9, "one billion"),
            (10**12, "one trillion"),
            (10**30, "one nonillion"),
            (10**33, "one decillion"),
            # Negative numbers
            (-0, "zero"),
            (-(10**2), "minus one hundred"),
            (-(10**3), "minus one thousand"),
            (-(10**6), "minus one million"),
            (-(10**9), "minus one billion"),
            (-(10**12), "minus one trillion"),
            (-(10**30), "minus one nonillion"),
            (-(10**33), "minus one decillion"),
            # Numbers less than 20
            (1, "one"),
            (2, "two"),
            (10, "ten"),
            (18, "eighteen"),
            (19, "nineteen"),
            # Multiples of 10
            (20, "twenty"),
            (30, "thirty"),
            (40, "forty"),
            (50, "fifty"),
            (60, "sixty"),
            (70, "seventy"),
            (80, "eighty"),
            (90, "ninety"),
            # Numbers less than 100
            (21, "twenty-one"),
            (32, "thirty-two"),
            (43, "forty-three"),
            (54, "fifty-four"),
            (65, "sixty-five"),
            (76, "seventy-six"),
            (87, "eighty-seven"),
            (98, "ninety-eight"),
            # Numbers less than 1000
            (100, "one hundred"),
            (101, "one hundred and one"),
            (110, "one hundred and ten"),
            (115, "one hundred and fifteen"),
            (120, "one hundred and twenty"),
            (121, "one hundred and twenty-one"),
            (700, "seven hundred"),
            (778, "seven hundred and seventy-eight"),
            (999, "nine hundred and ninety-nine"),
            # Complex numbers
            (87334, "eighty-seven thousand three hundred and thirty-four"),
            (
                54712671,
                "fifty-four million seven hundred and twelve thousand six hundred and seventy-one",
            ),
            (
                123456789,
                "one hundred and twenty-three million four hundred and fifty-six thousand seven hundred and eighty-nine",
            ),
            (
                999999999,
                "nine hundred and ninety-nine million nine hundred and ninety-nine thousand nine hundred and ninety-nine",
            ),
            (1000000000, "one billion"),
            (2000000000, "two billion"),
            (3000000000, "three billion"),
            # A few more edge cases
            (100010, "one hundred thousand and ten"),
            (201005, "two hundred and one thousand and five"),
            (712632000, "seven hundred and twelve million six hundred and thirty-two thousand"),
            (712632001, "seven hundred and twelve million six hundred and thirty-two thousand and one"),
            (-712632001, "minus seven hundred and twelve million six hundred and thirty-two thousand and one"),
            (
                913412708201001,
                "nine hundred and thirteen trillion four hundred and twelve billion seven hundred and eight million two hundred and one thousand and one",
            ),
            (13012008001001, "thirteen trillion twelve billion eight million one thousand and one"),
            (
                10**36 - 1,
                "nine hundred and ninety-nine decillion nine hundred and ninety-nine nonillion nine hundred and ninety-nine octillion nine hundred and ninety-nine septillion nine hundred and ninety-nine sextillion nine hundred and ninety-nine quintillion nine hundred and ninety-nine quadrillion nine hundred and ninety-nine trillion nine hundred and ninety-nine billion nine hundred and ninety-nine million nine hundred and ninety-nine thousand nine hundred and ninety-nine",
            ),
        ],
    )
    def test_number_to_words(self, number, expected):
        assert number_to_words(number) == expected
