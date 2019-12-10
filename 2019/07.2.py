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

    def __init__(self, amp_id):
        threading.Thread.__init__(self)
        self.id = amp_id
        self.input = input_queues[amp_id]
        self.output = input_queues[amp_id + 1]

        Amplifier.lock.acquire()
        input_file.seek(0)
        self.program = []
        line = input_file.read()
        for code in line.split(","):
            self.program.append(int(code))
        Amplifier.lock.release()

        self.param = MAX_PARAMS * [0]
        self.mode = MAX_PARAMS * [0]
        self.address = MAX_PARAMS * [0]

        self.pointer = 0
        self.opcode = self.program[self.pointer]
        self.instruction = self.opcode % 100
        self.opcode //= 100

    def print_debug(self, string):
        Amplifier.lock.acquire()
        print(string)
        print("Instance: {}".format(self.id))
        print("Program code: {} {} {} {}".format(self.program[self.pointer], self.program[self.pointer + 1],
                                                 self.program[self.pointer + 2], self.program[self.pointer + 3]))
        print("instruction: {}".format(self.instruction))
        print("params: {} {} {}".format(self.param[0], self.param[1], self.param[2]))
        print("modes: {} {} {}".format(self.mode[0], self.mode[1], self.mode[2]))
        print("addresses: {} {} {}".format(self.address[0], self.address[1], self.address[2]))
        print("input_queue: {}".format(self.input))
        Amplifier.lock.release()

    def run(self):
        try:
            while self.instruction != 99:
                if self.instruction in [1, 2, 7, 8]:
                    params_count = 3
                elif self.instruction in [5, 6]:
                    params_count = 2
                elif self.instruction in [3, 4]:
                    params_count = 1
                elif self.instruction == 99:
                    params_count = 0
                else:
                    self.print_debug("Unknown instruction: {}".format(self.instruction))
                    sys.exit(1)
                for param_id in range(params_count):
                    self.param[param_id] = self.program[self.pointer + param_id + 1]
                    self.mode[param_id] = self.opcode % 10
                    self.opcode //= 10
                    if self.mode[param_id] == 0:
                        self.address[param_id] = self.param[param_id]
                        self.param[param_id] = self.program[self.param[param_id]]
                if self.instruction == 1:
                    self.program[self.address[2]] = self.param[0] + self.param[1]
                elif self.instruction == 2:
                    self.program[self.address[2]] = self.param[0] * self.param[1]
                elif self.instruction == 3:
                    while len(self.input) == 0:
                        time.sleep(WAIT_TIME)
                    Amplifier.lock.acquire()
                    self.program[self.address[0]] = self.input[0]
                    del self.input[0]
                    Amplifier.lock.release()
                elif self.instruction == 4:
                    Amplifier.lock.acquire()
                    self.output.append(self.param[0])
                    Amplifier.lock.release()
                elif self.instruction == 5:
                    if self.param[0]:
                        params_count = self.param[1] - self.pointer - 1
                elif self.instruction == 6:
                    if not self.param[0]:
                        params_count = self.param[1] - self.pointer - 1
                elif self.instruction == 7:
                    if self.param[0] < self.param[1]:
                        self.program[self.address[2]] = 1
                    else:
                        self.program[self.address[2]] = 0
                elif self.instruction == 8:
                    if self.param[0] == self.param[1]:
                        self.program[self.address[2]] = 1
                    else:
                        self.program[self.address[2]] = 0
                self.pointer += params_count + 1
                self.opcode = self.program[self.pointer]
                self.instruction = self.opcode % 100
                self.opcode //= 100
        except Exception as e:
            self.print_debug("Error caught: {}".format(e.args[0]))
            sys.exit(1)
        running_threads[self.id] = 0


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
    input_queues = []
    running_threads = []
    for phase in current_phase_order:
        input_queues.append([phase])
        running_threads.append(0)
    input_queues.append(input_queues[0])
    input_queues[0].append(INPUT)

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
