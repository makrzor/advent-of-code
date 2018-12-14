#!/usr/bin/env python
from __future__ import print_function
import sys

if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    filename = sys.argv[0].split(".")[0] + ".txt"
input_file = open(filename, 'r')

def check_condition(list_len):
    if recipes[- search_len:] == search:
        print(list_len - search_len)
        exit(0)

search = []
recipes = [3, 7, 1, 0]
list_len = 4
i = 0
j = 1

for digit in input_file.read()[:-1]:
    search.append(int(digit))
search_len = len(search)

while True:
    sum = recipes[i] + recipes[j]
    if sum >= 10:
        recipes.append(1)
        sum -= 10
        list_len += 1
        check_condition(list_len)
    recipes.append(sum)
    list_len += 1
    check_condition(list_len)

    i += recipes[i] + 1
    if i >= list_len:
        i -= list_len
    j += recipes[j] + 1
    if j >= list_len:
        j -= list_len
