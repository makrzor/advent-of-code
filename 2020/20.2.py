#!/usr/bin/env python3

from __init__ import *

TILE_SIZE = 10
CUT_TILE_SIZE = 8
SEA_MONSTER_HORIZONTAL = [
    [18],
    [0, 5, 6, 11, 12, 17, 18, 19],
    [1, 4, 7, 10, 13, 16],
]
SEA_MONSTER_VERTICAL = [
    [1],
    [1, 2],
] + 3 * [
    [1],
    [0],
    [],
    [],
    [0],
    [1],
]
SMV_WIDTH = SMH_HEIGHT = len(SEA_MONSTER_HORIZONTAL)
SMH_WIDTH = SMV_HEIGHT = len(SEA_MONSTER_VERTICAL)
DIRECTIONS = [[1, 1], [1, -1], [-1, 1], [-1, -1]]


def string_to_int(row):
    number = 0
    for point in row:
        number *= 2
        if point == "#":
            number += 1
    return number


def get_row(array, row_number, direction="forwards"):
    if direction == "forwards":
        array_range = range(TILE_SIZE)
    else:
        array_range = range(TILE_SIZE - 1, -1, -1)
    return [array[row_number][j] for j in array_range]


def get_column(array, column_number, direction="forwards"):
    if direction == "forwards":
        array_range = range(TILE_SIZE)
    else:
        array_range = range(TILE_SIZE - 1, -1, -1)
    return [array[i][column_number] for i in array_range]


# flip == False:
# 0: 
# 1: T, Fh
# 2: Fh, Fv
# 3: T, Fv
# flip == True:
# 0: T
# 1: Fh
# 2: T, Fh, Fv
# 3: Fv
def rotate(tile_number, rotation, flip=False):
    tile = tiles[tile_number]
    # Following cut from back and bottom needed for minus coords logic
    tile = tile[:-1]
    for i in range(TILE_SIZE - 1):
        tile[i] = tile[i][:-1]
    if rotation in [1, 3]:
        transpose = True
    else:
        transpose = False
    if flip:
        transpose = not transpose
    if rotation in [1, 2]:
        row_modifier = -1
    else:
        row_modifier = 1
    if rotation in [2, 3]:
        column_modifier = -1
    else:
        column_modifier = 1
    new_tile = []
    for i in range(1, CUT_TILE_SIZE + 1):
        new_tile.append([])
        for j in range(1, CUT_TILE_SIZE + 1):
            if transpose:
                point = tile[row_modifier * j][column_modifier * i]
            else:
                point = tile[row_modifier * i][column_modifier * j]
            new_tile[-1].append(point)
    return new_tile


def tile_place(tile_number, rotation, flip=False, new_row=False):
    tile_data = rotate(tile_number, rotation, flip)
    if new_row:
        for _ in range(CUT_TILE_SIZE):
            waters.append([])
    for i in range(- CUT_TILE_SIZE, 0):
        waters[i].extend(tile_data[i])
    if flip:
        border_bank = 1
        right_border_number = (6 - rotation) % 4
        bottom_border_number = (5 - rotation) % 4
    else:
        border_bank = 0
        right_border_number = (5 - rotation) % 4
        bottom_border_number = (6 - rotation) % 4
    right_border = tile_borders[tile_number][border_bank][right_border_number]
    bottom_border = tile_borders[tile_number][border_bank][bottom_border_number]
    del tile_borders[tile_number]
    del tiles[tile_number]
    return right_border, bottom_border


def is_there_a_monster(x, y, monster, direction):
    for i in range(len(monster)):
        for j in monster[i]:
            if waters[x + i * direction[0]][y + j * direction[1]] != "#":
                return False
    return True


def find_monsters():
    for monster, monster_height, monster_width in [(SEA_MONSTER_HORIZONTAL, SMH_HEIGHT, SMH_WIDTH), (SEA_MONSTER_VERTICAL, SMV_HEIGHT, SMV_WIDTH)]:
        rows_to_check = waters_height - monster_height + 1
        columns_to_check = waters_width - monster_width + 1
        for direction in DIRECTIONS:
            locations = []
            for x in range(1 * direction[0], rows_to_check * direction[0], direction[0]):
                for y in range(1 * direction[1], columns_to_check * direction[1], direction[1]):
                    if is_there_a_monster(x, y, monster, direction):
                        locations.append([x, y])
            if locations:
                return monster, direction, locations


def evaporate_monsters(monster, direction, locations):
    for location in locations:
        for i in range(len(monster)):
            for j in monster[i]:
                waters[location[0] + i * direction[0]][location[1] + j * direction[1]] = "O"


def calculate_roughness():
    roughness = 0
    for x in range(waters_height):
        for y in range(waters_width):
            if waters[x][y] == "#":
                roughness += 1
    return roughness


tile_borders = {}
tiles = {}
waters = []

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
    tiles[tile_number] = []
    for i in range(TILE_SIZE):
        tiles[tile_number].append([])
        for j in range(TILE_SIZE):
            tiles[tile_number][-1].append(tile_lines[i][j])

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
corner_tiles = []
for tile_number, borders in tile_borders.items():
    borders_not_matched = []
    for i in range(len(borders[0])):
        for tile_number_to_match, border_to_match in tile_borders.items():
            if tile_number_to_match == tile_number:
                continue
            elif borders[0][i] in border_to_match[0] + border_to_match[1]:
                break
        else:
            borders_not_matched.append(i)
    if len(borders_not_matched) == 2:
        corner_tiles.append(tile_number)
        if len(corner_tiles) == 1:
            if borders_not_matched[1] == borders_not_matched[0] + 1:
                border_to_take = 0
            else:
                border_to_take = 1
            new_row_border_to_find = tile_borders[tile_number][0][borders_not_matched[border_to_take]]

max_column = len(tiles)
last_row = False
while True and not last_row:
    column = 0
    while column <= max_column:
        if column:
            new_row = False
            rotation_shift = 4
        else:
            new_row = True
            border_to_find = new_row_border_to_find
            rotation_shift = 3
        for tile_number_to_match, border_to_match in tile_borders.items():
            if border_to_find in border_to_match[0] + border_to_match[1]:
                break
        flip = True
        for i in range(2):
            for border in range(4):
                if tile_borders[tile_number_to_match][i][border] == border_to_find:
                    if i:
                        flip = False
                        rotation_shift = 7 - rotation_shift
                    rotation = (rotation_shift - border) % 4
        border_to_find, bottom_border = tile_place(tile_number_to_match, rotation, flip, new_row)
        if not column:
            new_row_border_to_find = bottom_border
        if tile_number_to_match in corner_tiles[1:]:
            if column:
                max_column = column
            else:
                last_row = True
        column += 1
# Following insert at front and top needed for minus coords logic
for i in range(len(waters)):
    waters[i].insert(0, ".")
waters.insert(0, len(waters[0]) * ["."])
waters_height = len(waters)
waters_width = len(waters[0])
evaporate_monsters(*find_monsters())
print(calculate_roughness())
