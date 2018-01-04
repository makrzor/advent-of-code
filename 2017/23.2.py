#!/usr/bin/env python

COPROCESSOR_PROGRAM = "set b 99,\
set c b,\
jnz a 2,\
jnz 1 5,\
mul b 100,\
sub b -100000,\
set c b,\
sub c -17000,\
set f 1,\
set d 2,\
set e 2,\
set g d,\
mul g e,\
sub g b,\
jnz g 2,\
set f 0,\
sub e -1,\
set g e,\
sub g b,\
jnz g -8,\
sub d -1,\
set g d,\
sub g b,\
jnz g -13,\
jnz f 2,\
sub h -1,\
set g b,\
sub g c,\
jnz g 2,\
jnz 1 3,\
sub b -17,\
jnz 1 -23"

program = COPROCESSOR_PROGRAM.split(',')
size = len(program)
registers = [0] * (ord('z') + 1)
registers[ord('a')] = 1
pointer = 0
jumped = 0

while pointer >= 0 and pointer < size:
    instruction = program[pointer].split()
    print(pointer, instruction, end=" ")
    if instruction[2].islower():
        instruction[2] = registers[ord(instruction[2])]
    else:
        instruction[2] = int(instruction[2])
    print(instruction[2], instruction[1], end=": ")
    if instruction[0] == 'jnz' and not instruction[1].islower():
        registers[ord(instruction[1])] = int(instruction[1])
    if instruction[0] == 'set':
        registers[ord(instruction[1])] = instruction[2]
    elif instruction[0] == 'sub':
        registers[ord(instruction[1])] -= instruction[2]
    elif instruction[0] == 'mul':
        registers[ord(instruction[1])] *= instruction[2]
    elif instruction[0] == 'jnz' and registers[ord(instruction[1])] != 0:
        pointer += instruction[2]
        jumped = 1
    if jumped == 0:
        pointer += 1
    else:
        jumped = 0
    print(registers[ord(instruction[1])])
#    print(registers[ord('h')])
