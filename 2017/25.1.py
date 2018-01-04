#!/usr/bin/env python

COMPONENTS = "32/31,\
2/2,\
0/43,\
45/15,\
33/24,\
20/20,\
14/42,\
2/35,\
50/27,\
2/17,\
5/45,\
3/14,\
26/1,\
33/38,\
29/6,\
50/32,\
9/48,\
36/34,\
33/50,\
37/35,\
12/12,\
26/13,\
19/4,\
5/5,\
14/46,\
17/29,\
45/43,\
5/0,\
18/18,\
41/22,\
50/3,\
4/4,\
17/1,\
40/7,\
19/0,\
33/7,\
22/48,\
9/14,\
50/43,\
26/29,\
19/33,\
46/31,\
3/16,\
29/46,\
16/0,\
34/17,\
31/7,\
5/27,\
7/4,\
49/49,\
14/21,\
50/9,\
14/44,\
29/29,\
13/38,\
31/11"

available = []

def walk(pins, available, strength, max_strength, length, max_length):
    for i in range(len(available)):
        component = available[i]
        if component[0] == pins:
            new_pins = component[1]
        elif component[1] == pins:
            new_pins = component[0]
        else:
            continue
        new_length = length + 1
        new_strength = strength + component[0] + component[1]
        if new_length >= max_length:
            max_length = new_length
            if new_strength > max_strength:
                max_strength = new_strength
        (new_max_s, new_max_l) = walk(new_pins, available[:i] + available[i + 1:], new_strength, max_strength, new_length, max_length)
        if new_max_l >= max_length:
            max_length = new_max_l
            if new_max_s > max_strength:
                max_strength = new_max_s
    return max_strength, max_length

for i in COMPONENTS.split(','):
    available.append([int(n) for n in i.split('/')])

print(walk(0, available, 0, 0, 0, 0)[0])
