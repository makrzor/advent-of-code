#!/usr/bin/env python
import sys

if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    filename = sys.argv[0].split(".")[0] + ".txt"
input_file = open(filename, 'r')

MAX_PARAMS = 3
PAINT_MODE = 0
MOVE_MODE = 1
MOVES = [(0, -1), (1, 0), (0, 1), (-1, 0)]


def print_debug(string):
    print(string)
    print("Program code: {} {} {} {}".format(program[pointer], program[pointer + 1],
                                             program[pointer + 2], program[pointer + 3]))
    print("instruction: {}".format(instruction))
    print("params: {} {} {}".format(param[0], param[1], param[2]))
    print("modes: {} {} {}".format(param_mode[0], param_mode[1], param_mode[2]))
    print("addresses: {} {} {}".format(address[0], address[1], address[2]))
    print("relative_base: {}".format(relative_base))


grid = [x[:] for x in [[-1] * 100] * 100]
x = y = 0
program = [0] * 10000
pointer = 0
line = input_file.read()
for code in line.split(","):
    program[pointer] = int(code)
    pointer += 1

mode = PAINT_MODE
direction = 0
colored_panels_count = 0
relative_base = 0
param = MAX_PARAMS * [0]
param_mode = MAX_PARAMS * [0]
address = MAX_PARAMS * [0]

pointer = 0
opcode = program[pointer]
instruction = opcode % 100
opcode //= 100

try:
    while instruction != 99:
        if instruction in [1, 2, 7, 8]:
            params = 3
        elif instruction in [5, 6]:
            params = 2
        elif instruction in [3, 4, 9]:
            params = 1
        elif instruction == 99:
            params = 0
        else:
            print_debug("Unknown instruction: {}".format(instruction))
            sys.exit(1)
        for i in range(params):
            param[i] = program[pointer + i + 1]
            param_mode[i] = opcode % 10
            opcode //= 10
            modifier = 0
            if param_mode[i] == 2:
                modifier = relative_base
            if param_mode[i] != 1:
                param[i] += modifier
                address[i] = param[i]
                param[i] = program[param[i]]
        if instruction == 1:
            program[address[2]] = param[0] + param[1]
        elif instruction == 2:
            program[address[2]] = param[0] * param[1]
        elif instruction == 3:
            program[address[0]] = int(grid[y][x] > 0)
        elif instruction == 4:
            if mode == PAINT_MODE:
                if grid[y][x] < 0:
                    colored_panels_count += 1
                if 0 <= param[0] <= 1:
                    grid[y][x] = param[0]
                else:
                    print_debug("Unknown color: {}".format(param[0]))
                    sys.exit(1)
            elif mode == MOVE_MODE:
                if param[0] == 0:
                    direction -= 1
                elif param[0] == 1:
                    direction += 1
                else:
                    print_debug("Unknown rotation: {}".format(param[0]))
                    sys.exit(1)
                direction %= len(MOVES)
                x += MOVES[direction][0]
                y += MOVES[direction][1]
            else:
                print_debug("Unknown mode: {}".format(mode))
                sys.exit(1)
            mode = 1 - mode
        elif instruction == 5:
            if param[0]:
                params = param[1] - pointer - 1
        elif instruction == 6:
            if not param[0]:
                params = param[1] - pointer - 1
        elif instruction == 7:
            if param[0] < param[1]:
                program[address[2]] = 1
            else:
                program[address[2]] = 0
        elif instruction == 8:
            if param[0] == param[1]:
                program[address[2]] = 1
            else:
                program[address[2]] = 0
        elif instruction == 9:
            relative_base += param[0]
        pointer += params + 1
        opcode = program[pointer]
        instruction = opcode % 100
        opcode //= 100
except Exception as e:
    print_debug("Error caught: {}".format(e.args[0]))
    sys.exit(1)

print(colored_panels_count)
