#!/usr/bin/env python

LENGTHS = "129,154,49,198,200,133,97,254,41,6,2,1,255,0,191,108"
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

number_list = [0] * LIST_SIZE
position = 0
skip = 0
addition = ""
for i in range(LIST_SIZE):
    number_list[i] = i
for char in ADDITIONAL_LENGTHS.split(','):
    addition += chr(int(char))
for length in (LENGTHS + addition) * 64:
    number_list = reverse(number_list, position, ord(length))
    position += ord(length) + skip
    if position >= LIST_SIZE:
        position -= LIST_SIZE
    skip += 1
    LENGTHS += ADDITIONAL_LENGTHS
dense = [0] * 16
knot_hash = ""
for i in range(16):
    for j in range(16 * i, 16 * (i + 1)):
        dense[i] ^= number_list[j]
    knot_hash += '%02x' % dense[i]
print(knot_hash)
