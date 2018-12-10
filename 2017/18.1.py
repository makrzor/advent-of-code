#!/usr/bin/env python

DUET = "set i 31,\
set a 1,\
mul p 17,\
jgz p p,\
mul a 2,\
add i -1,\
jgz i -2,\
add a -1,\
set i 127,\
set p 735,\
mul p 8505,\
mod p a,\
mul p 129749,\
add p 12345,\
mod p a,\
set b p,\
mod b 10000,\
snd b,\
add i -1,\
jgz i -9,\
jgz a 3,\
rcv b,\
jgz b -1,\
set f 0,\
set i 126,\
rcv a,\
rcv b,\
set p a,\
mul p -1,\
add p b,\
jgz p 4,\
snd a,\
set a b,\
jgz 1 3,\
snd b,\
set f 1,\
add i -1,\
jgz i -11,\
snd a,\
jgz f -16,\
jgz a -19"

program = DUET.split(',')
size = len(program)
registers = [0] * (ord('z') + 1)
pointer = 0
jumped = 0

while pointer >= 0 and pointer < size:
    instruction = program[pointer].split()
    if instruction[0] == 'snd' or instruction[0] == 'rcv':
        instruction.append(instruction[1])
    if instruction[2].islower():
        instruction[2] = registers[ord(instruction[2])]
    else:
        instruction[2] = int(instruction[2])
    if instruction[0] == 'snd':
        sound = instruction[2]
    elif instruction[0] == 'set':
        registers[ord(instruction[1])] = instruction[2]
    elif instruction[0] == 'add':
        registers[ord(instruction[1])] += instruction[2]
    elif instruction[0] == 'mul':
        registers[ord(instruction[1])] *= instruction[2]
    elif instruction[0] == 'mod':
        registers[ord(instruction[1])] %= instruction[2]
    elif instruction[0] == 'rcv' and instruction[2] != 0:
        registers[ord(instruction[1])] = sound
        print(sound)
        break
    elif instruction[0] == 'jgz' and registers[ord(instruction[1])] > 0:
        pointer += instruction[2]
        jumped = 1
    if jumped == 0:
        pointer += 1
    else:
        jumped = 0
