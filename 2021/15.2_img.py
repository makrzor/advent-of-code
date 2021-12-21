#!/usr/bin/env python3

from PIL import Image, ImageColor
from __init__ import *


def point_append(risk: int) -> None:
    point = {"risk": risk}
    for d in DIRECTIONS:
        point[d] = MAX
    cavern_map[-1].append(point)


MAX = 65535
INSPECTION_LEVEL = 9
DIRECTIONS = ["n", "e", "s", "w"]
cavern_map = [[]]
if len(sys.argv) > 1:
    filename = ".".join(sys.argv[1].split(".")[:-1]) + ".png"
else:
    filename = os.path.basename(".".join(sys.argv[0].split(".")[:2])) + ".png"

for line in get_input_stream():
    cavern_map.append([{}])
    for n in line.strip():
        point_append(int(n))
    width = len(cavern_map[-1]) - 1
    for _ in range(width * 4):
        new_n = cavern_map[-1][-width]["risk"] + 1
        if new_n > 9:
            new_n = 1
        point_append(new_n)
    cavern_map[-1].append({})
width = len(cavern_map[-1]) - 2
height = len(cavern_map) - 1
for _ in range(height * 4):
    cavern_map.append([{}])
    for column in range(1, width + 1):
        new_n = cavern_map[-height - 1][column]["risk"] + 1
        if new_n > 9:
            new_n = 1
        point_append(new_n)
    cavern_map[-1].append({})
cavern_map.append([])
height = len(cavern_map) - 2
cavern_map[height][width]["e"] = 0
cavern_map[height][width]["s"] = 0
for i in range(width + 2):
    cavern_map[0].append({})
    cavern_map[-1].append({})

for i in range(INSPECTION_LEVEL):
    for row in range(height, 0, -1):
        for column in range(width, 0, -1):
            me = cavern_map[row][column]
            e_neighbour = cavern_map[row][column + 1]
            s_neighbour = cavern_map[row + 1][column]
            if e_neighbour:
                me["e"] = e_neighbour["risk"] + min(e_neighbour[direction] for direction in DIRECTIONS)
            if s_neighbour:
                me["s"] = s_neighbour["risk"] + min(s_neighbour[direction] for direction in DIRECTIONS)

    for row in range(1, height + 1):
        for column in range(1, width + 1):
            me = cavern_map[row][column]
            n_neighbour = cavern_map[row - 1][column]
            w_neighbour = cavern_map[row][column - 1]
            if n_neighbour:
                me["n"] = n_neighbour["risk"] + min(n_neighbour[direction] for direction in DIRECTIONS)
            if w_neighbour:
                me["w"] = w_neighbour["risk"] + min(w_neighbour[direction] for direction in DIRECTIONS)

print(min(cavern_map[1][1][direction] for direction in DIRECTIONS))
image = Image.new("1", (width + 1, height + 1))
green = ImageColor.getcolor("green", "1")
x = 1
y = 1
image.putpixel((x, y), green)
while x < width or y < height:
    direction = sorted(cavern_map[y][x], key=cavern_map[y][x].get)[1]
    if direction == "e":
        x += 1
    elif direction == "s":
        y += 1
    elif direction == "w":
        x -= 1
    elif direction == "n":
        y -= 1
    else:
        print("ERROR")
    print(x, y)
    image.putpixel((x, y), green)
image.save(filename)
sys.exit(EXIT_SUCCESS)
