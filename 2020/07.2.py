#!/usr/bin/env python3

import re

from __init__ import *

SEARCHED_BAG = "shiny gold bag"
NULL_BAG = "no other bag"
BAG_STRING_REGEX = r"(\d+ )?([a-z]+ [a-z]+ bag)"

def count_contained_bags(bag):
    if bag == NULL_BAG:
        return 0
    bags_sum = 0
    for bag_name, bags_count in contents[bag]:
        bags_sum += bags_count * count_contained_bags(bag_name)
    return bags_sum + 1

contents = {}

for line in get_input_stream():
    bags = re.findall(BAG_STRING_REGEX, line)
    contents[bags[0][1]] = []
    for bags_count_text, bag_name in bags[1:]:
        if bag_name == NULL_BAG:
            contained_bags_count = -1
        else:
            contained_bags_count = int(bags_count_text)
        contents[bags[0][1]].append([bag_name, contained_bags_count])

print(count_contained_bags(SEARCHED_BAG) - 1)
