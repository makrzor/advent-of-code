#!/usr/bin/env python

import os
import sys

EXIT_SUCCESS = 0


def bin_digit_list_to_dec(bin_digit_list: list):
    return int("".join([str(digit) for digit in bin_digit_list]), 2)


def get_input_stream():
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = os.path.basename(sys.argv[0]).split(".")[0] + ".txt"
    return open(filename, 'r')


def transpose(array: list):
    return list(map(list, zip(*array)))
