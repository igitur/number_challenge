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

INVALID_NUMBER_STRING = "number invalid"
NEGATIVE_NUMBER_PREFIX = "minus"


def number_to_words(n: int) -> str:
    # A few shorcuts first
    if n == 0:
        return "zero"

    if n < 0:
        return NEGATIVE_NUMBER_PREFIX + " " + number_to_words(-n)

    base_10_exponent = math.log10(n)

    # if the number is a power of 10, return the corresponding word
    if base_10_exponent.is_integer():
        if int(base_10_exponent) in LARGE_NUMBER_NAMES:
            return "one " + LARGE_NUMBER_NAMES[int(base_10_exponent)]

    return INVALID_NUMBER_STRING
