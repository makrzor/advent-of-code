#!/usr/bin/env python3

from __init__ import *

MOVES = 10000000
DESTINATION_LIMIT = 1000001
DIMINISHED_CUPS_SIZE = 999997
INPUT_SIZE = 9

cups_list = [int(char) for char in get_input_stream().read().strip()] + [number for number in range(INPUT_SIZE + 1, DESTINATION_LIMIT)]
cups = {}
for i in range(-1, DESTINATION_LIMIT - 2):
    cups[cups_list[i]] = {
        'prev': cups_list[i - 1],
        'next': cups_list[i + 1],
    }
index = cups_list[0]
for _ in range(MOVES):
    extracted_start = cups[index]['next']
    extracted_end = cups[cups[extracted_start]['next']]['next']
    next_index = cups[extracted_end]['next']
    cups[index]['next'] = next_index
    cups[next_index]['prev'] = index
    destination = index - 1
    while destination == extracted_start or destination == extracted_end or destination == cups[extracted_start]['next'] or not destination:
        if not destination:
            destination = DESTINATION_LIMIT
        destination -= 1
    next_destination = cups[destination]['next']
    cups[next_destination]['prev'] = extracted_end
    cups[extracted_end]['next'] = next_destination
    cups[extracted_start]['prev'] = destination
    cups[destination]['next'] = extracted_start
    index = next_index
print(cups[1]['next'] * cups[cups[1]['next']]['next'])
