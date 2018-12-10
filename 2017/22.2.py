#!/usr/bin/env python

MAP = "...###.#.#.##...##.#..##.,\
.#...#..##.#.#..##.#.####,\
#..#.#...######.....#####,\
.###.#####.#...#.##.##...,\
.#.#.##......#....#.#.#..,\
....##.##.#..##.#...#....,\
#...###...#.###.#.#......,\
..#..#.....##..####..##.#,\
#...#..####.#####...#.##.,\
###.#.#..#..#...##.#..#..,\
.....##..###.##.#.....#..,\
#.....#...#.###.##.##...#,\
.#.##.##.##.#.#####.##...,\
##.#.###..#.####....#.#..,\
#.##.#...#.###.#.####..##,\
#.##..#..##..#.##.####.##,\
#.##.#....###.#.#......#.,\
.##..#.##..###.#..#...###,\
#..#.#.#####.....#.#.#...,\
.#####..###.#.#.##..#....,\
###..#..#..##...#.#.##...,\
..##....##.####.....#.#.#,\
..###.##...#..#.#####.###,\
####.########.#.#..##.#.#,\
#####.#..##...####.#..#.."
SIZE = 1000

grid = []
news = ((-1, 0), (0, 1), (1, 0), (0, -1))

map_split = MAP.split(',')
for i in range(len(map_split)):
    submap = map_split[i]
    grid.append([])
    for j in range(len(submap)):
        grid[i].append(submap[j])
    for j in range(len(submap), SIZE):
        grid[i].append('.')
for i in range(len(map_split), SIZE):
    grid.append([])
    for j in range(SIZE):
        grid[i].append('.')

position = [len(map_split) // 2, len(map_split) // 2]
direction = 0
infected = 0

for i in range(10000000):
    if grid[position[0]][position[1]] == '#':
        direction += 1
        grid[position[0]][position[1]] = 'F'
    elif grid[position[0]][position[1]] == 'F':
        direction += 2
        grid[position[0]][position[1]] = '.'
    elif grid[position[0]][position[1]] == '.':
        direction += 3
        grid[position[0]][position[1]] = 'W'
    else:
        grid[position[0]][position[1]] = '#'
        infected += 1
    direction %= 4
    position[0] += news[direction][0]
    position[1] += news[direction][1]
    position[0] %= SIZE
    position[1] %= SIZE
print(infected)
