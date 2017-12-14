#!/usr/bin/env python

LENGTHS = "hxtvlmkl-"
ADDITIONAL_LENGTHS = "17, 31, 73, 47, 23"
LIST_SIZE = 256
shadow_list = [0] * LIST_SIZE

def reverse(number_list, position, length):
    for i in range(0, length):
        a = (position + i) % LIST_SIZE
        b = (position + length - 1 - i) % LIST_SIZE
        shadow_list[a] = number_list[b]
    for i in range(0, length):
        a = (position + i) % LIST_SIZE
        number_list[a] = shadow_list[a]
    return number_list

grid = ""
for suffix in range(128):
    number_list = [0] * LIST_SIZE
    position = 0
    skip = 0
    addition = ""
    row = LENGTHS + str(suffix)
    for i in range(LIST_SIZE):
        number_list[i] = i
    for char in ADDITIONAL_LENGTHS.split(','):
        addition += chr(int(char))
    for length in (row + addition) * 64:
        number_list = reverse(number_list, position, ord(length))
        position += ord(length) + skip
        if position >= LIST_SIZE:
            position -= LIST_SIZE
        skip += 1
        row += ADDITIONAL_LENGTHS
    dense = [0] * 16
    knot_hash = ""
    for i in range(16):
        for j in range(16 * i, 16 * (i + 1)):
            dense[i] ^= number_list[j]
        knot_hash += '{0:b}'.format(dense[i]).zfill(8)
    grid += knot_hash
print(grid.count('1'))
