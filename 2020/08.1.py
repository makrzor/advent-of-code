#!/usr/bin/env python3

import re

from __init__ import *


def print_debug(string):
    print(string)
    print("pointer: {}".format(pointer))
    print("Program code: {}".format(program[pointer]))


program = []
for line in get_input_stream():
    line = line.strip()
    code = line.split()
    program.append([code[0], code[1:]])

visited = []
pointer = 0
accumulator = 0

try:
    while pointer not in visited:
        visited.append(pointer)
        instruction, params = program[pointer]
        if instruction == "acc":
            accumulator += int(params[0])
        elif instruction == "jmp":
            pointer += int(params[0]) - 1
        elif instruction == "nop":
            pass
        else:
            print_debug("Unknown instruction: {}".format(instruction))
            sys.exit(1)
        pointer += 1
except Exception as e:
    print_debug("Error caught: {}".format(e.args[0]))
    sys.exit(1)

print(accumulator)
