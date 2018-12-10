#!/usr/bin/env python

h = 0
for b in range(109900, 126917, 17):
    f = 1
    for d in range(2, b):
        for e in range(2, b):
            if d * e == b:
                f = 0
                break
        if f == 0:
            h += 1
            break
    print(b, d, e, h)
print(h)
