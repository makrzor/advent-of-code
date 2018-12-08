#!/usr/bin/env python
import sys

if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    filename = sys.argv[0].split(".")[0] + ".txt"
input_file = open(filename, 'r')

parent_node = [-1]
quantity_of_child_nodes = []
quantity_of_metadata_entries = []
node = 0
header = 0
metadata_sum = 0

line = input_file.read()
numbers = line.split()
quantity_of_numbers = len(numbers)
i = 0
while i < quantity_of_numbers:
    number = int(numbers[i])
    i += 1
    if header == 0:
        quantity_of_child_nodes.append(number)
        header = 1
    elif header == 1:
        quantity_of_metadata_entries.append(number)
        header = 2
    elif header == 2:
        i -= 1
        if quantity_of_child_nodes[node] > 0:
            quantity_of_child_nodes[node] -= 1
            parent_node.append(node)
            node = len(parent_node) - 1
            header = 0
        else:
            header = 3
    elif header == 3:
        if quantity_of_metadata_entries[node] > 0:
            quantity_of_metadata_entries[node] -= 1
            metadata_sum += number
        if quantity_of_metadata_entries[node] == 0:
            if parent_node[node] > -1:
                node = parent_node[node]
                header = 2
            else:
                print(metadata_sum)
                exit(0)
