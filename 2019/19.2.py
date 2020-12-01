#!/usr/bin/env python
import sys

if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    filename = sys.argv[0].split(".")[0] + ".txt"
input_file = open(filename, 'r')

MAX_PARAMS = 3
X_SIZE = Y_SIZE = 100
FULL_BEAM = 2 * X_SIZE + 2 * Y_SIZE - 4


def print_debug(string):
    print(string)
    print("Program code: {} {} {} {}".format(program[pointer], program[pointer + 1],
                                             program[pointer + 2], program[pointer + 3]))
    print("instruction: {}".format(instruction))
    print("params: {} {} {}".format(param[0], param[1], param[2]))
    print("modes: {} {} {}".format(mode[0], mode[1], mode[2]))
    print("addresses: {} {} {}".format(address[0], address[1], address[2]))
    print("relative_base: {}".format(relative_base))


line = input_file.read()

new_x_init = new_y_init = 0
x_or_y = 0
points_affected = 0
space = [x[:] for x in [[0] * 1000] * 1000]

try:
    while points_affected < FULL_BEAM:
        # print("Starting at {}, {}".format(new_x_init, new_y_init))
        x_init = new_x_init
        y_init = new_y_init
        new_x_init = new_y_init = 0
        x_max = x_init + X_SIZE
        y_max = y_init + Y_SIZE
        x = x_init
        y = y_init
        last_x_in_beam = x
        last_y_in_beam = y
        points_affected = 0
        while y < y_max:
            program = [0] * 10000
            pointer = 0
            for code in line.split(","):
                program[pointer] = int(code)
                pointer += 1

            relative_base = 0
            param = MAX_PARAMS * [0]
            mode = MAX_PARAMS * [0]
            address = MAX_PARAMS * [0]

            pointer = 0
            opcode = program[pointer]
            instruction = opcode % 100
            opcode //= 100

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
                    mode[i] = opcode % 10
                    opcode //= 10
                    modifier = 0
                    if mode[i] == 2:
                        modifier = relative_base
                    if mode[i] != 1:
                        param[i] += modifier
                        address[i] = param[i]
                        param[i] = program[param[i]]
                if instruction == 1:
                    program[address[2]] = param[0] + param[1]
                elif instruction == 2:
                    program[address[2]] = param[0] * param[1]
                elif instruction == 3:
                    program[address[0]] = (x, y)[x_or_y]
                    if x_or_y:
                        x_or_y = 0
                    else:
                        x_or_y = 1
                elif instruction == 4:
                    points_affected += param[0]
                    if param[0]:
                        # print("#", end="", flush=True)
                        if y == y_max - 1 and new_x_init == 0:
                            new_x_init = x
                            # print("x set to {}".format(new_x_init), end="")
                        if x == x_max - 1 and new_y_init == 0:
                            new_y_init = y
                            # print("y set to {}".format(new_y_init), end="")
                        last_x_in_beam = x
                        last_y_in_beam = y
                    # else:
                    #     print(".", end="", flush=True)
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
            if y == y_init or y == y_max - 1:
                x += 1
            else:
                if x == x_init:
                    x = x_max - 1
                else:
                    x = x_max
            if x == x_max:
                # print()
                x = x_init
                y += 1
        # print(points_affected)
        if new_x_init == 0:
            new_x_init = last_x_in_beam
            # print("x set to {}".format(new_x_init), end="")
        if new_y_init == 0:
            new_y_init = last_y_in_beam
            # print("y set to {}".format(new_y_init), end="")
except Exception as e:
    print_debug("Error caught: {}".format(e.args[0]))
    sys.exit(1)

print(new_x_init * 10000 + new_y_init)
