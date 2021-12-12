#!/usr/bin/env python3

from __init__ import *


def add_path(path_start: str, path_end: str) -> None:
    if path_start != LAST_CAVE and path_end != STARTING_CAVE:
        if path_start not in caves:
            caves[path_start] = []
        caves[path_start].append(path_end)


def count_paths(cave: str) -> int:
    if cave == LAST_CAVE:
        return 1
    visited_caves.append(cave)
    paths_count = 0
    for next_cave in caves[cave]:
        if next_cave.lower() not in visited_caves:
            paths_count += count_paths(next_cave)
    visited_caves.pop()
    return paths_count


STARTING_CAVE = "start"
LAST_CAVE = "end"
caves = {}

for line in get_input_stream():
    first_cave, second_cave = line.strip().split("-")
    add_path(first_cave, second_cave)
    add_path(second_cave, first_cave)

visited_caves = []

print(count_paths(STARTING_CAVE))
sys.exit(EXIT_SUCCESS)
