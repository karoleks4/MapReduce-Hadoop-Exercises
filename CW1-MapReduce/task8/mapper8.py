#!/usr/bin/python

import sys

for line in sys.stdin:
	line = line.strip().split()
	if len(line) > 5:
		print(line)