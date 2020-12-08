#!/usr/bin/env python3

import re

from __init__ import *


def print_debug(string):
    print(string)
    print("pointer: {}".format(pointer))
    print("Program code: {}".format(program[pointer]))


def nop_jmp_switch(pointer):
    if program[pointer][0] == "nop":
        program[pointer][0] = "jmp"
    elif program[pointer][0] == "jmp":
        program[pointer][0] = "nop"

def program_run():
    visited = []
    pointer = 0
    accumulator = 0
    try:
        while pointer not in visited and pointer != program_stop_pointer:
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
    if pointer == program_stop_pointer:
        return accumulator
    else:
        return None


program = []
for line in get_input_stream():
    line = line.strip()
    code = line.split()
    program.append([code[0], code[1:]])
program_stop_pointer = len(program)

return_value = None
pointer_to_be_changed = 0
while return_value is None:
    nop_jmp_switch(pointer_to_be_changed)
    return_value = program_run()
    nop_jmp_switch(pointer_to_be_changed)
    pointer_to_be_changed += 1
print(return_value)
