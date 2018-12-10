#!/usr/bin/env python
import sys

if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    filename = sys.argv[0].split(".")[0] + ".txt"
input_file = open(filename, 'r')

def count_value(node):
    value = 0
    if len(child_nodes[node]) > 0:
        for index in indexes[node]:
            if index <= len(child_nodes[node]):
                value += count_value(child_nodes[node][index - 1])
    else:
        for index in indexes[node]:
            value += index
    return value

parent_node = [-1]
quantity_of_child_nodes = []
quantity_of_metadata_entries = []
node = 0
header = 0
child_nodes = []
indexes = []

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
            if len(child_nodes) <= node:
                child_nodes.append([])
                indexes.append([])
            if len(child_nodes) > node:
                quantity_of_child_nodes[node] -= 1
                parent_node.append(node)
                child_nodes[node].append(len(parent_node) - 1)
                node = child_nodes[node][-1]
                header = 0
        else:
            header = 3
    elif header == 3:
        if quantity_of_metadata_entries[node] > 0:
            if len(indexes) <= node:
                indexes.append([])
            if len(indexes) > node:
                quantity_of_metadata_entries[node] -= 1
                indexes[node].append(number)
        if quantity_of_metadata_entries[node] == 0:
            if parent_node[node] > -1:
                node = parent_node[node]
                header = 2
            else:
                break

print(count_value(0))
