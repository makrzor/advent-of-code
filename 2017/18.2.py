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
registers = [[0] * (ord('z') + 1), [0] * (ord('z') + 1)]
registers[1][ord('p')] = 1
pointer = [0] * 2
jumped = [0] * 2
waiting = [0] * 2
instance = 1
send = [[], []]
sent = [0] * 2

while waiting[0] == 0 or len(send[1]) > 0 or waiting[1] == 0 or len(send[0]) > 0:
    if pointer[1 - instance] != -1 and (waiting[1 - instance] == 0 or len(send[instance]) > 0):
        instance ^= 1
    instruction = program[pointer[instance]].split()
#    print instruction[1], registers[instance][ord(instruction[1])]
#    print instance, pointer[instance], instruction
    if instruction[0] == 'snd' or instruction[0] == 'rcv':
        instruction.append(instruction[1])
    if instruction[2].islower():
        instruction[2] = registers[instance][ord(instruction[2])]
    else:
        instruction[2] = int(instruction[2])
    if instruction[0] == 'snd':
#        print instance, "to", 1 - instance, send[instance], "len:", len(send[instance])
        send[instance].append(instruction[2])
#        print instance, "to", 1 - instance, send[instance], "len:", len(send[instance])
        sent[instance] += 1
#        if sent[instance] == 10:
#            break
    elif instruction[0] == 'set':
        registers[instance][ord(instruction[1])] = instruction[2]
    elif instruction[0] == 'add':
        registers[instance][ord(instruction[1])] += instruction[2]
    elif instruction[0] == 'mul':
        registers[instance][ord(instruction[1])] *= instruction[2]
    elif instruction[0] == 'mod':
        registers[instance][ord(instruction[1])] %= instruction[2]
    elif instruction[0] == 'rcv':
#        print 1 - instance, "to", instance, send[1 - instance], "len:", len(send[1 - instance])
        if len(send[1 - instance]) > 0:
            registers[instance][ord(instruction[1])] = send[1 - instance].pop(0)
            waiting[instance] = 0
        else:
            waiting[instance] = 1
#            print instance, "set to WAIT"
#        print 1 - instance, "to", instance, send[1 - instance], "len:", len(send[1 - instance])
    elif instruction[0] == 'jgz':
        if instruction[1].islower():
            instruction[1] = registers[instance][ord(instruction[1])]
        if instruction[1] > 0:
            pointer[instance] += instruction[2]
            jumped[instance] = 1
    if jumped[instance] == 0 and waiting[instance] == 0:
        pointer[instance] += 1
    else:
        jumped[instance] = 0
#    print instruction[1], registers[instance][ord(instruction[1])]
    if pointer[instance] < 0 or pointer[instance] >= size:
        pointer[instance] = -1
        if pointer[1 - instance] == -1:
            break
#print
print sent[1]
