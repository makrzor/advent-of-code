#!/usr/bin/env python

LENGTHS = "129,154,49,198,200,133,97,254,41,6,2,1,255,0,191,108"
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
for i in range(LIST_SIZE):
    number_list[i] = i
for length in LENGTHS.split(','):
    number_list = reverse(number_list, position, int(length))
    position += int(length) + skip
    if position >= LIST_SIZE:
        position -= LIST_SIZE
    skip += 1
print(number_list[0] * number_list[1])
