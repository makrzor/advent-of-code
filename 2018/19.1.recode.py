#!/usr/bin/env python

registers = [0] * 6

#ip 1
0: jump(17)                                                    #addi 1 16 1
.1: registers[2] = 1                                            #seti 1 8 2
.2: registers[4] = 1                                            #seti 1 5 4
.3: registers[3] = registers[2] * registers[4]                  #mulr 2 4 3
4: registers[3] = 1 if registers[3] == registers[5] else 0     #eqrr 3 5 3
5: jump(7) if registers[3] == 1                                #addr 3 1 1
6: jump(8)                                                     #addi 1 1 1
.7: registers[0] += registers[2]                                #addr 2 0 0
.8: registers[4] += 1                                           #addi 4 1 4
9: registers[3] = 1 if registers[4] > registers[5] else 0      #gtrr 4 5 3
10: jump(12) if registers[3] == 1                               #addr 1 3 1
11: jump(3)                                                     #seti 2 8 1
.12: registers[2] += 1                                           #addi 2 1 2
13: registers[3] = 1 if registers[2] > registers[5] else 0      #gtrr 2 5 3
14: jump(16) if registers[3] == 1                               #addr 3 1 1
15: jump(2)                                                     #seti 1 8 1
.16: exit(0)                                                     #mulr 1 1 1
.17: registers[5] += 2                                           #addi 5 2 5
18: registers[5] *= registers[5]                                #mulr 5 5 5
19: registers[5] *= 19                                          #mulr 1 5 5
20: registers[5] *= 11                                          #muli 5 11 5
21: registers[3] += 5                                           #addi 3 5 3
22: registers[3] *= 22                                          #mulr 3 1 3
23: registers[3] += 4                                           #addi 3 4 3
24: registers[5] += registers[3]                                #addr 5 3 5
25: jmp(26) + registers[0]                                      #addr 1 0 1
.26: jump(1)                                                     #seti 0 7 1
.27: registers[3] = 27                                           #setr 1 1 3
.28: registers[3] *= 28                                          #mulr 3 1 3
.29: registers[3] += 29                                          #addr 1 3 3
.30: registers[3] *= 30                                          #mulr 1 3 3
.31: registers[3] *= 14                                          #muli 3 14 3
.32: registers[3] *= 32                                          #mulr 3 1 3
.33: registers[5] += registers[3]                                #addr 5 3 5
.34: registers[0] = 0                                            #seti 0 9 0
.35: jump(1)                                                     #seti 0 0 1
.36: ...
