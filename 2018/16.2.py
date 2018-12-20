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

def addr(a, b, c):
    return addi(a, registers[b], c)

def addi(a, b, c):
    registers[c] = registers[a] + b

def mulr(a, b, c):
    return muli(a, registers[b], c)

def muli(a, b, c):
    registers[c] = registers[a] * b

def banr(a, b, c):
    return bani(a, registers[b], c)

def bani(a, b, c):
    registers[c] = registers[a] & b

def borr(a, b, c):
    return bori(a, registers[b], c)

def bori(a, b, c):
    registers[c] = registers[a] | b

def setr(a, b, c):
    return seti(registers[a], b, c)

def seti(a, b, c):
    registers[c] = a

def gtir(a, b, c):
    if a > registers[b]:
        registers[c] = 1
    else:
        registers[c] = 0

def gtri(a, b, c):
    if registers[a] > b:
        registers[c] = 1
    else:
        registers[c] = 0

def gtrr(a, b, c):
    return gtri(a, registers[b], c)

def eqir(a, b, c):
    return eqri(b, a, c)

def eqri(a, b, c):
    if registers[a] == b:
        registers[c] = 1
    else:
        registers[c] = 0

def eqrr(a, b, c):
    return eqri(a, registers[b], c)

empty_count = 0

for line in input_file:
    if line[:-1] == "":
        empty_count += 1
    else:
        empty_count = 0
    if empty_count > 2:
        break

for line in input_file:
    instruction = line.split()
    opcode = int(instruction[0])
    a = int(instruction[1])
    b = int(instruction[2])
    c = int(instruction[3])
    if opcode == 0:
        eqir(a, b, c)
    elif opcode == 1:
        addi(a, b, c)
    elif opcode == 2:
        gtir(a, b, c)
    elif opcode == 3:
        setr(a, b, c)
    elif opcode == 4:
        mulr(a, b, c)
    elif opcode == 5:
        seti(a, b, c)
    elif opcode == 6:
        muli(a, b, c)
    elif opcode == 7:
        eqri(a, b, c)
    elif opcode == 8:
        bori(a, b, c)
    elif opcode == 9:
        bani(a, b, c)
    elif opcode == 10:
        gtrr(a, b, c)
    elif opcode == 11:
        eqrr(a, b, c)
    elif opcode == 12:
        addr(a, b, c)
    elif opcode == 13:
        gtri(a, b, c)
    elif opcode == 14:
        borr(a, b, c)
    elif opcode == 15:
        banr(a, b, c)
    else:
        print("Error: Unknown opcode:", opcode)
        exit(1)
print(registers[0])
exit(0)
