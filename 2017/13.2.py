#!/usr/bin/env python

FIREWALL = "0: 3,\
1: 2,\
2: 6,\
4: 4,\
6: 4,\
8: 8,\
10: 6,\
12: 8,\
14: 5,\
16: 6,\
18: 8,\
20: 8,\
22: 12,\
24: 6,\
26: 9,\
28: 8,\
30: 12,\
32: 12,\
34: 17,\
36: 12,\
38: 8,\
40: 12,\
42: 12,\
44: 10,\
46: 12,\
48: 12,\
50: 12,\
52: 14,\
54: 14,\
56: 10,\
58: 14,\
60: 12,\
62: 14,\
64: 14,\
66: 14,\
68: 14,\
70: 14,\
72: 14,\
74: 14,\
76: 14,\
86: 14,\
94: 20,\
96: 18"

for delay in range(0, 2000000000, 2):
    severity = 0
    for layer in FIREWALL.split(','):
        (depth, scanner_range) = [int(i) for i in layer.split(':')]
        if (depth + delay) % (2 * (scanner_range - 1)) == 0:
            if depth == 0:
                depth = 1
            severity += depth * scanner_range
    if delay % 131072 == 0:
        print("[{}...]".format(delay))
    if severity == 0:
        break
print(delay, severity)