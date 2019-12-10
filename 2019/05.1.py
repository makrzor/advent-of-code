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
    print("i: {}".format(i))


program = []
line = input_file.read()
for code in line.split(","):
    program.append(int(code))

input = 1
output = 0
param = MAX_PARAMS * [0]
mode = MAX_PARAMS * [0]
address = MAX_PARAMS * [0]

pointer = 0
opcode = program[pointer]
instruction = opcode % 100
opcode //= 100

try:
    while instruction != 99:
        if instruction == 1 or instruction == 2:
            params = MAX_PARAMS
        elif instruction != 99:
            params = 1
        else:
            params = 0
        for i in range(params):
            param[i] = program[pointer + i + 1]
            mode[i] = opcode % 10
            opcode //= 10
            if mode[i] == 0:
                address[i] = param[i]
                param[i] = program[param[i]]
        if instruction == 1:
            program[address[2]] = param[0] + param[1]
            jump = 4
        elif instruction == 2:
            program[address[2]] = param[0] * param[1]
            jump = 4
        elif instruction == 3:
            program[address[0]] = input
            jump = 2
        elif instruction == 4:
            output = param[0]
            jump = 2
        else:
            print_debug("Unknown instruction: {}".format(instruction))
            sys.exit(1)
        pointer += jump
        opcode = program[pointer]
        instruction = opcode % 100
        opcode //= 100
except Exception as e:
    print_debug("Error caught: {}".format(e.args[0]))
    sys.exit(1)

print(output)
