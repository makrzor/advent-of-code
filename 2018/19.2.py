#!/usr/bin/env python

a = 0
c = 10551350
for i in range(1, c + 1):
    if c % i == 0:
        a += i
print(a)
exit(0)
