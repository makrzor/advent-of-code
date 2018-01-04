#!/usr/bin/env python

INITIAL_PATTERN = (".#.", "..#", "###")

def mirror_h(a, b, c = None):
    if c is None:
        return a[::-1], b[::-1]
    else:
        return a[::-1], b[::-1], c[::-1]

def mirror_v(a, b, c = None):
    if c is None:
        return b, a
    else:
        return c, b, a

def rot(a, b, c = None):
    if c is None:
        return a[1] + b[1], a[0] + b[0]
    else:
        return a[2] + b[2] + c[2], a[1] + b[1] + c[1], a[0] + b[0] + c[0]

def twothree(a, b):
    if a == ".." and b == "..":
        return "...", "...", "..#'
    elif a == "##" and b == "##":
        return "#.#", "...", "#.."
    elif (a + b).count('#') == 1:
        return "#.#", "..#", "..."
    elif (a + b).count('#') == 3:
        return "###", "#.#", "..#"
    elif a == ".." or b == ".." or a == b:
        return "#.#", "..#", "#.#"
    else:
        return "#..", "...", ".##"

def threefour(a, b, c):
    if a == "....":
        return "....", ".##.", "#...", ".##."
    else:
        mapping = {".#..": ("...#", "##.#", "#.#.", "#..."),
                   "....": ("..##", "###.", "..##", "#..."),
                   ".#.#": ("...#", "##..", "...#", "##.#"),
                   "..##": ("...#", "..##", "#.##", "##.#"),
                   "...#": ("#...", "..##", "###.", "#..#"),
                   ".###": ("..##", ".###", "###.", "..#.")}
        return mapping[c]

pattern = INITIAL_PATTERN
steps = 0

while steps < 18:
    new_pattern = [[]] * len(pattern)
    for i in (0, len(pattern), 3):
        for j in (0, len(pattern), 3):
            new_pattern[i].append(threefour(pattern[3 * i][3 * j:3 * j + 3],
                                            pattern[3 * i + 1][3 * j:3 * j + 3],
                                            pattern[3 * i + 2][3 * j:3 * j + 3]))
    pattern = new_pattern
    steps += 1
    new_pattern = [[]] * len(pattern)
    for i in (0, len(pattern), 2):
        for j in (0, len(pattern), 2):
            new_pattern[i].append(twothree(pattern[2 * i][2 * j:2 * j + 2],
                                           pattern[2 * i + 1][2 * j:2 * j + 2]))
    pattern = new_pattern
    steps += 1

'''
3       5
4       9
6       16
9       38
12      71
18      164
27      
36
54
81
108
162
243
324
486
729
972
1458
2187
'''
