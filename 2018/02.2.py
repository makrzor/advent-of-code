#!/usr/bin/env python

input_file = open("02.txt", 'r')

boxes = []

for box in input_file:
    boxes.append(box)
for i in range(len(boxes)):
    box_a = boxes[i]
    for j in range(i + 1, len(boxes)):
        box_b = boxes[j]
        differences = 0
        for i in range(len(box_a)):
            if box_a[i] != box_b[i]:
                differences += 1
                if differences == 2:
                    break
        if differences == 1:
            for i in range(len(box_a)):
                if box_a[i] != box_b[i]:
                    break
            print(box_a[:i] + box_a[i + 1:])
            exit(0)
