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
for i in range(25):
    submap = map_split[i]
    grid.append([])
    for j in range(len(submap)):
        grid[i].append(submap[j])
    for j in range(len(submap), SIZE):
        grid[i].append('.')
for i in range(25, SIZE):
    grid.append([])
    for j in range(SIZE):
        grid[i].append('.')

position = [12, 12]
direction = 0
infected = 0

for i in range(10000):
#    print(len(grid[position[0]]))
#    print(position)
    if grid[position[0]][position[1]] == '#':
        direction += 1
        grid[position[0]][position[1]] = '.'
    else:
        direction -= 1
        grid[position[0]][position[1]] = '#'
        infected += 1
    direction %= 4
    position[0] += news[direction][0]
    position[1] += news[direction][1]
    position[0] %= SIZE
    position[1] %= SIZE
print(infected)
