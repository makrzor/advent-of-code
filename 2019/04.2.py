#!/usr/bin/env python
import sys

if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    filename = sys.argv[0].split(".")[0] + ".txt"
input_file = open(filename, 'r')

PASSWORD_LENGTH = 6
MIN = 10 ** (PASSWORD_LENGTH - 1)
MAX = 10 ** PASSWORD_LENGTH - 1
password_dissolved = [0 for pos in range(PASSWORD_LENGTH)]
passwords_valid = 0

line = input_file.read()
(start, stop) = (int(password) for password in line.split("-"))

if start < MIN:
    start = MIN
if stop > MAX:
    stop = MAX

password = start
while password <= stop:
    pass_work = password
    for i in range(PASSWORD_LENGTH):
        password_dissolved[- i - 1] = pass_work % 10
        pass_work //= 10
    spotted_double = False
    failed_condition = False
    for i in range(PASSWORD_LENGTH - 1):
        if password_dissolved[i] > password_dissolved[i + 1]:
            failed_condition = True
            break
        elif password_dissolved[i] == password_dissolved[i + 1] \
                and (i == 0 and password_dissolved[i + 1] != password_dissolved[i + 2]
                     or i == PASSWORD_LENGTH - 2 and password_dissolved[i - 1] != password_dissolved[i]
                     or password_dissolved[i - 1] != password_dissolved[i] != password_dissolved[i + 2]):
            spotted_double = True
    if spotted_double and not failed_condition:
        passwords_valid += 1
    password += 1

print(passwords_valid)
