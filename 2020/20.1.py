#!/usr/bin/env python3

from __init__ import *


def string_to_int(row):
    number = 0
    for point in row:
        number *= 2
        if point == "#":
            number += 1
    return number


def get_row(array, row_number, direction="forwards"):
    if direction == "forwards":
        array_range = range(len(array[row_number]))
    else:
        array_range = range(len(array[row_number]) - 1, -1, -1)
    return [array[row_number][j] for j in array_range]


def get_column(array, column_number, direction="forwards"):
    if direction == "forwards":
        array_range = range(len(array))
    else:
        array_range = range(len(array) - 1, -1, -1)
    return [array[i][column_number] for i in array_range]


tile_borders = {}

input_data = get_input_stream().read()
tiles_data = input_data.split("\n\n")
for tile_data in tiles_data:
    if not tile_data:
        continue
    tile_lines = tile_data.split("\n")
    if not tile_lines[-1]:
        tile_lines = tile_lines[:-1]
    tile_number = int(tile_lines[0][5:-1])
    tile_lines = tile_lines[1:]
    tile_borders[tile_number] = [
        [
            string_to_int(get_row(tile_lines, 0)),
            string_to_int(get_column(tile_lines, -1)),
            string_to_int(get_row(tile_lines, -1, "backwards")),
            string_to_int(get_column(tile_lines, 0, "backwards"))
        ], [
            string_to_int(get_row(tile_lines, 0, "backwards")),
            string_to_int(get_column(tile_lines, -1, "backwards")),
            string_to_int(get_row(tile_lines, -1)),
            string_to_int(get_column(tile_lines, 0)),
        ],
    ]
product = 1
for tile_number, borders in tile_borders.items():
    borders_not_matched_count = 0
    for border in borders[0]:
        for tile_number_to_match, border_to_match in tile_borders.items():
            if tile_number_to_match == tile_number:
                continue
            elif border in border_to_match[0] + border_to_match[1]:
                break
        else:
            borders_not_matched_count += 1
    if borders_not_matched_count == 2:
        product *= tile_number
print(product)
