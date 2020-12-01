#!/usr/bin/env python
import sys

if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    filename = sys.argv[0].split(".")[0] + ".txt"
input_file = open(filename, 'r')

MAX_PARAMS = 3
ROOM_SIZE = 100
INPUT_MAP = {"w": 1, "s": 2, "a": 3, "d": 4}
DIRECTIONS_MAP = {"w": (0, -1), "s": (0, 1), "a": (-1, 0), "d": (1, 0)}
MARK_MAP = {-3: "X", -2: "D", -1: " ", 0: "#", 1: ".", 2: "O"}


def print_debug(string):
    print(string)
    print("Program code: {} {} {} {}".format(program[pointer], program[pointer + 1],
                                             program[pointer + 2], program[pointer + 3]))
    print("instruction: {}".format(instruction))
    print("params: {} {} {}".format(param[0], param[1], param[2]))
    print("modes: {} {} {}".format(mode[0], mode[1], mode[2]))
    print("addresses: {} {} {}".format(address[0], address[1], address[2]))
    print("relative_base: {}".format(relative_base))


def print_room():
    print("{}-{}, {}-{}".format(most_left_position, most_right_position, most_up_position, most_down_position))
    for y in range(most_up_position, most_down_position + 1):
        for x in range(most_left_position, most_right_position + 1):
            if x == 0 and y == 0:
                mark = -3
            elif x == droid_x and y == droid_y and sealed_room[x][y] != 2:
                mark = -2
            else:
                mark = sealed_room[x][y]
            print(MARK_MAP[mark], end="")
        print()


program = [0] * 10000
pointer = 0
line = input_file.read()
for code in line.split(","):
    program[pointer] = int(code)
    pointer += 1

output = 0
sealed_room = [x[:] for x in [[-1] * ROOM_SIZE] * ROOM_SIZE]
droid_x = droid_y = 0
move = (0, 0)
most_left_position = most_up_position = most_right_position = most_down_position = 0

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
            print_room()
            user_input = ""
            while user_input not in INPUT_MAP.keys():
                user_input = input("Move: ")
            move = DIRECTIONS_MAP[user_input]
            program[address[0]] = INPUT_MAP[user_input]
        elif instruction == 4:
            if droid_x + move[0] < most_left_position:
                most_left_position = droid_x + move[0]
            elif droid_x + move[0] > most_right_position:
                most_right_position = droid_x + move[0]
            elif droid_y + move[1] < most_up_position:
                most_up_position = droid_y + move[1]
            elif droid_y + move[1] > most_down_position:
                most_down_position = droid_y + move[1]
            if param[0] == 0:
                sealed_room[droid_x + move[0]][droid_y + move[1]] = 0
                print("Wall to the {}".format(move))
            elif param[0] == 1 or param[0] == 2:
                print("Moved {}".format(move))
                droid_x, droid_y = droid_x + move[0], droid_y + move[1]
                sealed_room[droid_x][droid_y] = param[0]
                if param[0] == 2:
                    print_room()
                    sys.exit(0)
            else:
                print_debug("Unknown output: {}".format(param[0]))
                sys.exit(1)
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

print(output)
