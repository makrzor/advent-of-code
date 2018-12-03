#!/usr/bin/env python

input_file = open("01.txt", 'r')

frequency = 0
frequencies_visited = [0] * 1000000
frequencies_visited[0] = 1

while(True):
    for frequency_change in input_file:
        frequency += int(frequency_change)
        if frequencies_visited[frequency] == 1:
            print(frequency)
            exit(0)
        frequencies_visited[frequency] = 1
    input_file.seek(0)
