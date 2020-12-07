#!/usr/bin/env python3

import re

from __init__ import *

SEARCHED_BAG = "shiny gold bag"
BAG_STRING_REGEX = "[a-z]+ [a-z]+ bag"

is_content_of = {}

for line in get_input_stream():
    bags = re.findall(BAG_STRING_REGEX, line)
    for contained_bag in bags[1:]:
        if contained_bag in is_content_of:
            is_content_of[contained_bag].add(bags[0])
        else:
            is_content_of[contained_bag] = {bags[0]}

can_contain_shiny_gold_bag = is_content_of[SEARCHED_BAG]
bags_to_be_reviewed = is_content_of[SEARCHED_BAG]
bags_to_be_added = set()

while bags_to_be_reviewed:
    for bag in bags_to_be_reviewed:
        for bag_to_be_added in is_content_of.get(bag, []):
            if bag_to_be_added not in can_contain_shiny_gold_bag:
                bags_to_be_added.add(bag_to_be_added)
    can_contain_shiny_gold_bag |= bags_to_be_added
    bags_to_be_reviewed = bags_to_be_added
    bags_to_be_added = set()

print(len(can_contain_shiny_gold_bag))
