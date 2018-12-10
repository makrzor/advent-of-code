#!/usr/bin/env python

FACTOR_A = 16807
FACTOR_B = 48271
DIVIDER = 2147483647
STARTER_A = 634
STARTER_B = 301
LIMIT = 40 * 1000 * 1000

matches = 0
reminder_a = STARTER_A
reminder_b = STARTER_B
for i in range(LIMIT):
    reminder_a = (reminder_a * FACTOR_A) % DIVIDER
    reminder_b = (reminder_b * FACTOR_B) % DIVIDER
    if "{0:x}".format(reminder_a)[-4:] == "{0:x}".format(reminder_b)[-4:]:
        matches += 1
print(matches)
