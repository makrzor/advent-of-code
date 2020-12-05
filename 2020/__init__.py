#!/usr/bin/env python
import os
import sys

EXIT_SUCCESS = 0

def get_input_stream():
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = os.path.basename(sys.argv[0]).split(".")[0] + ".txt"
    return open(filename, 'r')
