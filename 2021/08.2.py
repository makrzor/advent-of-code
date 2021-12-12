#!/usr/bin/env python3

from __init__ import *

SIMPLE_DIGIT_LENGTHS = {
    2: "1",
    3: "7",
    4: "4",
    7: "8",
}
FIVE_DIGIT_LENGTHS = {
    "1": "3",
    "4 - 1": "5",
    "8 - 4": "2",
}
SIX_DIGIT_LENGTHS = {
    "4": "9",
    "5": "6",
    "7": "0",
}


def contains(container: str, containee: str) -> bool:
    return False not in [c in container for c in containee]


def subtract(minuend: str, subtrahend: str) -> str:
    return "".join(c for c in minuend if c not in subtrahend)


total_sum = 0

for line in get_input_stream():
    full_digits, display_digits = [s.split() for s in line.split(" | ")]
    digits_decode = {}
    digits_encode = {}
    for digit in full_digits:
        digit_length = len(digit)
        if digit_length in SIMPLE_DIGIT_LENGTHS:
            digits_decode[digit] = SIMPLE_DIGIT_LENGTHS[digit_length]
            digits_encode[SIMPLE_DIGIT_LENGTHS[digit_length]] = digit
    for digit in digits_decode:
        full_digits.remove(digit)
    digits_encode["4 - 1"] = subtract(digits_encode["4"], digits_encode["1"])
    digits_encode["8 - 4"] = subtract(digits_encode["8"], digits_encode["4"])
    for digit in [digit for digit in full_digits if len(digit) == 5]:
        for digit_pattern in FIVE_DIGIT_LENGTHS:
            if contains(digit, digits_encode[digit_pattern]):
                digits_decode[digit] = FIVE_DIGIT_LENGTHS[digit_pattern]
                digits_encode[FIVE_DIGIT_LENGTHS[digit_pattern]] = digit
                break
        full_digits.remove(digit)
    for digit in full_digits:
        for digit_pattern in SIX_DIGIT_LENGTHS:
            if contains(digit, digits_encode[digit_pattern]):
                digits_decode[digit] = SIX_DIGIT_LENGTHS[digit_pattern]
                break

    number = ""
    for display_digit in display_digits:
        for digit in digits_decode:
            if contains(display_digit, digit) and contains(digit, display_digit):
                number += digits_decode[digit]
                break
    total_sum += int(number)

print(total_sum)
sys.exit(EXIT_SUCCESS)
