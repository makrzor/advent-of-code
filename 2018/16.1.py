#!/usr/bin/env python
from __future__ import print_function
import sys

if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    filename = sys.argv[0].split(".")[0] + ".txt"
input_file = open(filename, 'r')

registers = [0] * 4
registers_after = [0] * 4

def check_addr(a, b, c):
    return check_addi(a, registers[b], c)

def check_addi(a, b, c):
    if registers[a] + b == registers_after[c]:
        return True
    else:
        return False

def check_mulr(a, b, c):
    return check_muli(a, registers[b], c)

def check_muli(a, b, c):
    if registers[a] * b == registers_after[c]:
        return True
    else:
        return False

def check_banr(a, b, c):
    return check_bani(a, registers[b], c)

def check_bani(a, b, c):
    if registers[a] & b == registers_after[c]:
        return True
    else:
        return False

def check_borr(a, b, c):
    return check_bori(a, registers[b], c)

def check_bori(a, b, c):
    if registers[a] | b == registers_after[c]:
        return True
    else:
        return False

def check_setr(a, b, c):
    return check_seti(registers[a], b, c)

def check_seti(a, b, c):
    if a == registers_after[c]:
        return True
    else:
        return False

def check_gtir(a, b, c):
    if a > registers[b] and registers_after[c] == 1 or a <= registers[b] and registers_after[c] == 0:
        return True
    else:
        return False

def check_gtri(a, b, c):
    if registers[a] > b and registers_after[c] == 1 or registers[a] <= b and registers_after[c] == 0:
        return True
    else:
        return False

def check_gtrr(a, b, c):
    return check_gtri(a, registers[b], c)

def check_eqir(a, b, c):
    return check_eqri(b, a, c)

def check_eqri(a, b, c):
    if registers[a] == b and registers_after[c] == 1 or registers[a] != b and registers_after[c] == 0:
        return True
    else:
        return False

def check_eqrr(a, b, c):
    return check_eqri(a, registers[b], c)

samples_sum = 0

while True:
    line = input_file.readline()[:-1]
    if line != "":
        fragments = line.split()
        fragments[1] = fragments[1][1:]
        for i in range(4):
            registers[i] = int(fragments[i + 1][:-1])
        instruction = input_file.readline()[:-1].split()
        a = int(instruction[1])
        b = int(instruction[2])
        c = int(instruction[3])
        fragments = input_file.readline()[9:-1].split()
        for i in range(4):
            registers_after[i] = int(fragments[i][:-1])
        empty_line = input_file.readline()
        opcodes_like = 0
        if check_addr(a, b, c):
            opcodes_like += 1
        if check_addi(a, b, c):
            opcodes_like += 1
        if check_mulr(a, b, c):
            opcodes_like += 1
        if check_muli(a, b, c):
            opcodes_like += 1
        if check_banr(a, b, c):
            opcodes_like += 1
        if check_bani(a, b, c):
            opcodes_like += 1
        if check_borr(a, b, c):
            opcodes_like += 1
        if check_bori(a, b, c):
            opcodes_like += 1
        if check_setr(a, b, c):
            opcodes_like += 1
        if check_seti(a, b, c):
            opcodes_like += 1
        if check_gtir(a, b, c):
            opcodes_like += 1
        if check_gtri(a, b, c):
            opcodes_like += 1
        if check_gtrr(a, b, c):
            opcodes_like += 1
        if check_eqir(a, b, c):
            opcodes_like += 1
        if check_eqri(a, b, c):
            opcodes_like += 1
        if check_eqrr(a, b, c):
            opcodes_like += 1
        if opcodes_like >= 3:
            samples_sum += 1
    else:
        print(samples_sum)
        exit(0)
