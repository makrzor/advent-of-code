#!/usr/bin/env python

def increment_and_exit(a, c):
    for i in range(1, c + 1):
        if c % i == 0:
            a += i
    print(a)
    exit(0)

a = 1
b = 114
c = 950

if a == 0 or a == 9:
    increment_and_exit(a, c)
if a > 9:
    print(a)
    exit(0)
if a == 1:
    b = 27
if a < 3:
    b *= 28
if a < 4:
    b += 29
if a < 5:
    b *= 30
if a < 6:
    b *= 14
if a < 7:
    b *= 32
if a < 8:
    c += b
a = 0
increment_and_exit(a, c)
