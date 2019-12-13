#!/usr/bin/env python
import sys

if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    filename = sys.argv[0].split(".")[0] + ".txt"
input_file = open(filename, 'r')

MAX_PARAMS = 3


def print_debug(string):
    print(string)
    print("Program code: {} {} {} {}".format(program[pointer], program[pointer + 1],
                                             program[pointer + 2], program[pointer + 3]))
    print("instruction: {}".format(instruction))
    print("params: {} {} {}".format(param[0], param[1], param[2]))
    print("modes: {} {} {}".format(mode[0], mode[1], mode[2]))
    print("addresses: {} {} {}".format(address[0], address[1], address[2]))
    print("relative_base: {}".format(relative_base))


program = [0] * 10000
pointer = 0
line = input_file.read()
for code in line.split(","):
    program[pointer] = int(code)
    pointer += 1
program[0] = 2

input = 0
score = 0
output = [x[:] for x in [[0] * 100] * 100]
output_x = output_y = -2
current_ball_column = -1
current_paddle_column = -1
relative_base = 0
param = MAX_PARAMS * [0]
mode = MAX_PARAMS * [0]
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
            if current_ball_column != -1 != current_paddle_column:
                if current_ball_column < current_paddle_column:
                    input = -1
                elif current_ball_column > current_paddle_column:
                    input = 1
                else:
                    input = 0
            program[address[0]] = input
        elif instruction == 4:
            if output_x == -2:
                output_x = param[0]
            elif output_y == -2:
                output_y = param[0]
            elif output_x == -1 and output_y == 0:
                score = param[0]
                output_x = output_y = -2
            else:
                output[output_x][output_y] = param[0]
                if param[0] == 4:
                    current_ball_column = output_x
                elif param[0] == 3:
                    current_paddle_column = output_x
                output_x = output_y = -2
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

print(score)
