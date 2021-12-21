#!/usr/bin/env python3

from copy import deepcopy
from __init__ import *


def add(first_addend: list, second_addend: list) -> list:
    result = [deepcopy(first_addend), deepcopy(second_addend),
              max(first_addend[2], second_addend[2]) + 1,
              max(first_addend[3], second_addend[3])]
    return reduce(result)


def decode_one(text: str) -> list:
    if "," in text:
        output = decode_pair(text)
    else:
        value = int(text)
        output = [-1, value, 0, value]
    return output


def decode_pair(text: str) -> list:
    chunks = text[1:-1].split(",")
    if len(chunks) == 2:
        left_text, right_text = chunks
    else:
        brackets_sum = [0, 0]
        chunks_division = 1
        for k in range(len(chunks)):
            brackets_sum[0] += chunks[k].count("[")
            brackets_sum[1] += chunks[k].count("]")
            if brackets_sum[0] == brackets_sum[1]:
                break
            chunks_division += 1
        left_text = ",".join(chunks[:chunks_division])
        right_text = ",".join(chunks[chunks_division:])
    left_number = decode_one(left_text)
    right_number = decode_one(right_text)
    return [left_number, right_number,
            max(left_number[2], right_number[2]) + 1,
            max(left_number[3], right_number[3])]


def explode(number: list, level: int) -> list:
    if level == 1:
        output = (number[0][1], number[1][1])
        number[0] = -1
        number[1] = 0
        number[2] = 0
        number[3] = 0
    else:
        reduced_level = level - 1
        if number[0][2] == reduced_level:
            (left, right) = explode(number[0], reduced_level)
            if right:
                increase(number[1], right, 0)
            output = [left, 0]
        else:
            (left, right) = explode(number[1], reduced_level)
            if left:
                increase(number[0], 0, left)
            output = [0, right]
        number[2] = max(number[0][2], number[1][2]) + 1
        number[3] = max(number[0][3], number[1][3])
    return output


def increase(number: list, left: int, right: int) -> None:
    if number[0] == -1:
        number[1] += left + right
        number[3] = number[1]
    else:
        if left:
            increase(number[0], left, 0)
        elif right:
            increase(number[1], 0, right)
        number[3] = max(number[0][3], number[1][3])


def magnitude(number: list) -> int:
    if number[0] == -1:
        result = number[1]
    else:
        result = 3 * magnitude(number[0]) + 2 * magnitude(number[1])
    return result


def reduce(number: list) -> list:
    while number[2] > 4 or number[3] > 9:
        while number[2] > 4:
            explode(number, number[2])
        if number[3] > 9:
            split_leftmost(number)
    return number


def split_leftmost(number: list) -> None:
    if number[0] == -1:
        left_split = number[1] // 2
        right_split = number[1] - left_split
        number[0] = [-1, left_split, 0, left_split]
        number[1] = [-1, right_split, 0, right_split]
        number[2] = 1
        number[3] = right_split
    else:
        if number[0][3] > 9:
            split_leftmost(number[0])
        else:
            split_leftmost(number[1])
        number[2] = max(number[0][2], number[1][2]) + 1
        number[3] = max(number[0][3], number[1][3])


# number_structure:
# [0]: first of the pair (-1 for a regular number indication)
# [1]: second of the pair OR value of regular number if [0] == -1
# [2]: nest level
# [3]: highest value
numbers = []

for line in get_input_stream():
    numbers.append(decode_pair(line.strip()))

magnitudes = []
for i in range(len(numbers)):
    for j in range(len(numbers)):
        if i != j:
            magnitudes.append(magnitude(add(numbers[i], numbers[j])))

print(max(magnitudes))
sys.exit(EXIT_SUCCESS)
