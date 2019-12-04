#!/usr/bin/env python
import sys

if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    filename = sys.argv[0].split(".")[0] + ".txt"
input_file = open(filename, 'r')

program = []
line = input_file.read()
for code in line.split(","):
    program.append(int(code))

if len(program) > 12:
    program[1] = 12
    program[2] = 2

pointer = 0
opcode = program[pointer]

while opcode != 99:
    param_1 = program[program[pointer + 1]]
    param_2 = program[program[pointer + 2]]
    if opcode == 1:
        result = param_1 + param_2
    elif opcode == 2:
        result = param_1 * param_2
    else:
        print("Unknown opcode: {}".format(opcode))
        sys.exit(1)
    program[program[pointer + 3]] = result
    pointer += 4
    opcode = program[pointer]

print(program[0])
