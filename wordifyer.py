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


def validate(n) -> int:
    """
    Validates and sanitizes the input number.

    The input can be a string, int, or float, but it must represent a whole number.
    The number must be within the range of -(10**36 - 1) to (10**36 - 1).

    Args:
        n: The input value to validate.

    Returns:
        The validated integer.

    Raises:
        TypeError: If the input is not a numeric type or cannot be converted to an integer.
        ValueError: If the input number is outside the supported range.
    """
    if isinstance(n, str):
        try:
            n = int(n)
        except ValueError:
            raise TypeError("Input must be an integer")

    if not isinstance(n, (int, float)):
        raise TypeError("Input must be a numeric type")

    if not n.is_integer():
        raise TypeError("Input must be an integer")

    if abs(n) >= 10**36:
        raise ValueError("Input is outside the valid range")

    return n


def _base_10_exponent(n: int) -> int:
    """
    Calculates the base-10 exponent for a given integer.

    This is a helper function to determine the magnitude of a number. For very large
    numbers, it uses an iterative approach to avoid float precision issues.

    If the number is a perfect power of 10 (e.g., 1000), it returns an integer exponent.
    Otherwise, it returns a float to distinguish it from perfect powers.

    Args:
        n: The integer for which to find the exponent.

    Returns:
        The base-10 exponent, as an integer for perfect powers of 10, or a float
        otherwise.
    """
    if n < 10000000000:
        # use built-in approach. float is accurate enough here
        return math.log10(n)

    # For very large numbers, we need a different approach
    # We approximate the exponent by repeatedly dividing by 10
    exp = 0
    is_power_of_10 = True
    while n >= 10:
        if n % 10 != 0:
            is_power_of_10 = False
        n //= 10
        exp += 1

    # The exact fraction is irrelevant. Later on we just want to know whether it's an integer or has a fraction
    return exp + (0.5 if is_power_of_10 else 0)


def try_shortcut(n: int) -> tuple[bool, str | None]:
    """
    Attempts to find a direct word representation for a number.

    This handles atomic numbers (1-19), multiples of ten (10, 20, ... 90),
    and simple large number names (e.g., "one thousand", "one million").

    Args:
        n: The number to check.

    Returns:
        A tuple containing:
        - A boolean indicating if a shortcut was found.
        - The string representation if found, otherwise None.
    """
    if n in ATOMIC_NUMBER_NAMES:
        return True, ATOMIC_NUMBER_NAMES[n]

    if n in MULTIPLES_OF_TEN:
        return True, MULTIPLES_OF_TEN[n]

    base_10_exponent = _base_10_exponent(n)

    # if the number is a power of 10, return the corresponding word
    if base_10_exponent.is_integer():
        if int(base_10_exponent) in LARGE_NUMBER_NAMES:
            return True, "one " + LARGE_NUMBER_NAMES[int(base_10_exponent)]

    return False, None


def handle_less_than_100(n: int, prefix_and: bool) -> tuple[bool, list[str]]:
    """
    Converts a number between 20 and 99 into its word representation.

    It assumes `n` is not an atomic number or a simple multiple of ten, as those
    are handled by `try_shortcut`.

    Args:
        n: The number to convert (must be < 100).
        prefix_and: If True, prepends "and" to the list of words.

    Returns:
        A tuple containing:
        - A boolean indicating success (always True).
        - A list of strings representing the number in words.
    """
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
    """
    Converts a number between 100 and 999 into its word representation.

    It breaks the number into the hundreds part and the remainder, then
    recursively calls the conversion logic for the remainder.

    Args:
        n: The number to convert (must be < 1000).

    Returns:
        A tuple containing:
        - A boolean indicating success.
        - A list of strings representing the number in words.
    """
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
    """
    Recursively converts a number greater than or equal to 1000.

    It splits the number into the largest scale part (e.g., millions, thousands)
    and the remainder, then converts each part. For example, 54,712,671 is
    split into 54 (million) and 712,671.

    Args:
        n: The number to convert.

    Returns:
        A tuple containing:
        - A boolean indicating success.
        - A list of strings representing the number in words, or None on failure.
    """
    # We want to break up a number e.g. 54712671 into 54 and 712671
    # i.e. we look for the largest power of 1000
    # and we 'split' the value there.
    base_10_exponent = int(_base_10_exponent(n))
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

    # Usually we want a comma after a large number name (e.g. 7 million, three hundred thousand, four hundred and fifty)
    # but not if the next word is 'and' (e.g. one thousand and one) and we don't want a trailing comma
    needs_comma = len(part2_value) > 0 and part2_value[0] != "and"
    return True, part1_value + [LARGE_NUMBER_NAMES[magnitude] + ("," if needs_comma else "")] + part2_value


def try_convert(n: int, prefix_and: bool) -> tuple[bool, list[str]]:
    """
    Dispatches number conversion to the appropriate handler based on magnitude.

    This is the core recursive function that breaks down a number and converts it
    into a list of word components.

    Args:
        n: The number to convert.
        prefix_and: If True, an "and" may be prefixed for numbers less than 100
                    as part of a larger number (e.g., "one hundred AND one").

    Returns:
        A tuple containing:
        - A boolean indicating success.
        - A list of strings representing the number in words.
    """
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
    """
    Converts an integer into its English word representation.

    Handles positive and negative integers up to (but not including) 10**36.
    It uses the short scale for large number names (billion = 10**9).

    Args:
        n: The integer to convert. Can also be a string representation of an integer.

    Returns:
        The English word representation of the number as a string,
        or "number invalid" if the input is invalid or out of range.
    """
    try:
        n = validate(n)
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
