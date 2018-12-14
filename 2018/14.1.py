#!/usr/bin/env python
from __future__ import print_function
import sys

if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    filename = sys.argv[0].split(".")[0] + ".txt"
input_file = open(filename, 'r')

recipes = [3, 7, 1, 0]
list_len = 4
i = 0
j = 1

after = int(input_file.readline())
limit = after + 10

while list_len < limit:
    sum = recipes[i] + recipes[j]
    if sum >= 10:
        recipes.append(1)
        sum -= 10
        list_len += 1
    recipes.append(sum)
    list_len += 1

    i += recipes[i] + 1
    if i >= list_len:
        i -= list_len
    j += recipes[j] + 1
    if j >= list_len:
        j -= list_len
for i in range(after, limit):
    print(recipes[i], end="")
print()
