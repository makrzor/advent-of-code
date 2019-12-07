#!/usr/bin/env python
import sys
import threading
import time

if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    filename = sys.argv[0].split(".")[0] + ".txt"
input_file = open(filename, 'r')

MAX_PARAMS = 3
INPUT = 0
WAIT_TIME = 0

class Amplifier(threading.Thread):
    lock = threading.Lock()

    def __init__(self, number):
        threading.Thread.__init__(self)
        self.Number = number
        self.Input = input_queues[number]
        self.Output = input_queues[number + 1]

        Amplifier.lock.acquire()
        input_file.seek(0)
        self.Program = []
        line = input_file.read()
        for code in line.split(","):
            self.Program.append(int(code))
        Amplifier.lock.release()

        self.Param = MAX_PARAMS * [0]
        self.Mode = MAX_PARAMS * [0]
        self.Address = MAX_PARAMS * [0]

        self.Pointer = 0
        self.Opcode = self.Program[self.Pointer]
        self.Instruction = self.Opcode % 100
        self.Opcode //= 100

    def print_debug(self, string):
        Amplifier.lock.acquire()
        print(string)
        print("Instance: {}".format(self.Number))
        print("Program code: {} {} {} {}".format(self.Program[self.Pointer], self.Program[self.Pointer + 1],
                                                 self.Program[self.Pointer + 2], self.Program[self.Pointer + 3]))
        print("instruction: {}".format(self.Instruction))
        print("params: {} {} {}".format(self.Param[0], self.Param[1], self.Param[2]))
        print("modes: {} {} {}".format(self.Mode[0], self.Mode[1], self.Mode[2]))
        print("addresses: {} {} {}".format(self.Address[0], self.Address[1], self.Address[2]))
        print("input_queue: {}".format(self.Input))
        Amplifier.lock.release()

    def run(self):
        try:
            while self.Instruction != 99:
                if self.Instruction in [1, 2, 7, 8]:
                    params = 3
                elif self.Instruction in [5, 6]:
                    params = 2
                elif self.Instruction in [3, 4]:
                    params = 1
                elif self.Instruction == 99:
                    params = 0
                else:
                    self.print_debug("Unknown instruction: {}".format(self.Instruction))
                    sys.exit(1)
                for i in range(params):
                    self.Param[i] = self.Program[self.Pointer + i + 1]
                    self.Mode[i] = self.Opcode % 10
                    self.Opcode //= 10
                    if self.Mode[i] == 0:
                        self.Address[i] = self.Param[i]
                        self.Param[i] = self.Program[self.Param[i]]
                if self.Instruction == 1:
                    self.Program[self.Address[2]] = self.Param[0] + self.Param[1]
                elif self.Instruction == 2:
                    self.Program[self.Address[2]] = self.Param[0] * self.Param[1]
                elif self.Instruction == 3:
                    while len(self.Input) == 0:
                        time.sleep(WAIT_TIME)
                    Amplifier.lock.acquire()
                    self.Program[self.Address[0]] = self.Input[0]
                    del self.Input[0]
                    Amplifier.lock.release()
                elif self.Instruction == 4:
                    Amplifier.lock.acquire()
                    self.Output.append(self.Param[0])
                    Amplifier.lock.release()
                elif self.Instruction == 5:
                    if self.Param[0]:
                        params = self.Param[1] - self.Pointer - 1
                elif self.Instruction == 6:
                    if not self.Param[0]:
                        params = self.Param[1] - self.Pointer - 1
                elif self.Instruction == 7:
                    if self.Param[0] < self.Param[1]:
                        self.Program[self.Address[2]] = 1
                    else:
                        self.Program[self.Address[2]] = 0
                elif self.Instruction == 8:
                    if self.Param[0] == self.Param[1]:
                        self.Program[self.Address[2]] = 1
                    else:
                        self.Program[self.Address[2]] = 0
                self.Pointer += params + 1
                self.Opcode = self.Program[self.Pointer]
                self.Instruction = self.Opcode % 100
                self.Opcode //= 100
        except Exception as e:
            self.print_debug("Error caught: {}".format(e.args[0]))
            sys.exit(1)
        running_threads[self.Number] = 0


phase_orders = []
for number in range(56789, 98766):
    current_phase_order = [0, 0, 0, 0, 0]
    digit_sum = 0
    phases_ok = True
    phases = number
    for i in range(5):
        digit = phases % 10
        if digit < 5 or digit in current_phase_order[4 - i + 1:]:
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
    # print("Current phase order: {} ({})".format(current_phase_order, phase_order_number))
    input_queues = []
    running_threads = []
    for phase in current_phase_order:
        input_queues.append([phase])
        running_threads.append(0)
    input_queues.append(input_queues[0])
    input_queues[0].append(INPUT)
    # print("Input queues: {}".format(input_queues))

    threads = []
    for i in range(5):
        thread = Amplifier(i)
        thread.start()
        running_threads[i] = 1
        threads.append(thread)

    for i in range(5):
        threads[i].join()

    if input_queues[-1][0] > max_output:
        max_output = input_queues[-1][0]
        optimal_phase_order = phase_order_number
    phase_order_number += 1

print(max_output)
