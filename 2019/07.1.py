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


phase_orders = []
for number in range(1234, 43211):
    current_phase_order = [0, 0, 0, 0, 0]
    digit_sum = 0
    phases_ok = True
    phases = number
    for i in range(5):
        digit = phases % 10
        if digit > 4 or digit in current_phase_order[4 - i + 1:]:
            phases_ok = False
            break
        current_phase_order[4 - i] = digit
        digit_sum += digit
        phases //= 10
    if phases_ok:
        phase_orders.append(current_phase_order)

phase_order_number = 0
max_output = -999999
for current_phase_order in phase_orders:
    output = 0
    for phase in current_phase_order:
        input_queue = [phase, output]

        program = []
        line = input_file.read()
        for code in line.split(","):
            program.append(int(code))

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
                elif instruction in [3, 4]:
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
                    if mode[i] == 0:
                        address[i] = param[i]
                        param[i] = program[param[i]]
                if instruction == 1:
                    program[address[2]] = param[0] + param[1]
                elif instruction == 2:
                    program[address[2]] = param[0] * param[1]
                elif instruction == 3:
                    program[address[0]] = input_queue[0]
                    del input_queue[0]
                elif instruction == 4:
                    output = param[0]
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
                pointer += params + 1
                opcode = program[pointer]
                instruction = opcode % 100
                opcode //= 100
        except Exception as e:
            print_debug("Error caught: {}".format(e.args[0]))
            sys.exit(1)

        input_file.seek(0)

    if output > max_output:
        max_output = output
        optimal_phase_order = phase_order_number
    phase_order_number += 1

print(max_output)
