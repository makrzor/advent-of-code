#!/usr/bin/env python
import sys

if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    filename = sys.argv[0].split(".")[0] + ".txt"
input_file = open(filename, 'r')

line = input_file.read()
searched = 19690720

for noun in range(100):
    for verb in range(100):
        program = []
        for code in line.split(","):
            program.append(int(code))
        program[1] = noun
        program[2] = verb

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
                print("Unknown opcode: {} for noun {}, verb {}".format(opcode, noun, verb))
                sys.exit(1)
            program[program[pointer + 3]] = result
            pointer += 4
            opcode = program[pointer]

        if program[0] == searched:
            print("{}{}".format(noun, verb))
            sys.exit(0)
