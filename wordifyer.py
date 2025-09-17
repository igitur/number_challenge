import math

# We're assuming the short scale
# https://en.wikipedia.org/wiki/Long_and_short_scales

# https://en.wikipedia.org/wiki/Names_of_large_numbers
LARGE_NUMBER_NAMES = {
    2: "hundred",
    3: "thousand",
    6: "million",
    9: "billion",
    12: "trillion",
    15: "quadrillion",
    18: "quintillion",
    21: "sextillion",
    24: "septillion",
    27: "octillion",
    30: "nonillion",
    33: "decillion",
}


ATOMIC_NUMBER_NAMES = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    # 10 is included in MULTIPLES_OF_TEN
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
}

MULTIPLES_OF_TEN = {
    10: "ten",
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety",
}

INVALID_NUMBER_STRING = "number invalid"
NEGATIVE_NUMBER_PREFIX = "minus"


def validate(n: int) -> None:
    if not isinstance(n, (int, float)):
        raise TypeError("Input must be a numeric type")

    if not n.is_integer():
        raise TypeError("Input must be an integer")

    if abs(n) >= 10**36:
        raise ValueError("Input is outside the valid range")


def try_shortcut(n: int) -> tuple[bool, str | None]:
    if n in ATOMIC_NUMBER_NAMES:
        return True, ATOMIC_NUMBER_NAMES[n]

    if n in MULTIPLES_OF_TEN:
        return True, MULTIPLES_OF_TEN[n]

    base_10_exponent = math.log10(n)

    # if the number is a power of 10, return the corresponding word
    if base_10_exponent.is_integer():
        if int(base_10_exponent) in LARGE_NUMBER_NAMES:
            return True, "one " + LARGE_NUMBER_NAMES[int(base_10_exponent)]

    return False, None


def handle_less_than_100(n: int, prefix_and: bool) -> tuple[bool, list[str]]:
    # we know n is > 20 too (from previous shortcut approach)
    tens = (n // 10) * 10
    units = n % 10
    value = ["and"] if prefix_and else []
    if units == 0:
        value = value + [MULTIPLES_OF_TEN[tens]]
    else:
        value = value + [MULTIPLES_OF_TEN[tens] + "-" + ATOMIC_NUMBER_NAMES[units]]

    return True, value


def handle_less_than_1000(n: int) -> tuple[bool, list[str]]:
    hundreds = n // 100
    remainder = n % 100

    hundreds_value = ATOMIC_NUMBER_NAMES[hundreds] + " hundred"
    success, remainder_value = try_convert(remainder, prefix_and=True)

    if not success:
        # Then something went very wrong!
        return False, []

    if len(remainder_value) == 0:
        return True, [hundreds_value]

    return True, [hundreds_value] + remainder_value


def handle_conversion_recursively(n: int) -> tuple[bool, list[str]]:
    # We want to break up a number e.g. 54712671 into 54 and 712671
    # i.e. we look for the largest power of 1000
    # and we 'split' the value there.
    base_10_exponent = int(math.log10(n))
    magnitude = base_10_exponent - base_10_exponent % 3

    if magnitude not in LARGE_NUMBER_NAMES:
        return False, None

    part1 = n // 10**magnitude
    part2 = n % 10**magnitude

    success, part1_value = try_convert(part1, prefix_and=False)
    if not success:
        return False, None

    success, part2_value = try_convert(part2, prefix_and=True)
    if not success:
        return False, None

    return True, part1_value + [LARGE_NUMBER_NAMES[magnitude]] + part2_value


def try_convert(n: int, prefix_and: bool) -> tuple[bool, list[str]]:
    """
    Recursively convert a number into words.
    The prefix 'and' is used to separate the hundreds from the tens/units.
    e.g. "one hundred and twenty-three"
    """

    # We have already handled the pure zero case
    # If n is zero here, it's the remnant of parsing a bigger number.
    if n == 0:
        return True, []

    # The really simple cases
    success, value = try_shortcut(n)
    if success:
        if prefix_and:
            return True, ["and", value]

        return True, [value]

    if n < 100:
        return handle_less_than_100(n, prefix_and)

    if n < 1000:
        return handle_less_than_1000(n)

    # Now the real recursive stuff starts
    return handle_conversion_recursively(n)


def number_to_words(n: int) -> str:
    try:
        validate(n)
    except (TypeError, ValueError):
        return INVALID_NUMBER_STRING

    if n == 0:
        return "zero"

    if n < 0:
        return NEGATIVE_NUMBER_PREFIX + " " + number_to_words(-n)

    success, value = try_convert(n, prefix_and=False)
    if success:
        return " ".join(value)

    return INVALID_NUMBER_STRING
