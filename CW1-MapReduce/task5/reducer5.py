#!/usr/bin/python3

import sys

for i, line in enumerate(sys.stdin):
    if i <= 24:
        print(line.strip())