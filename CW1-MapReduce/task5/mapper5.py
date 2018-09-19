#!/usr/bin/python

import sys

for line in sys.stdin:
	tokens = line.strip().split()
	print('{0}\t{1} {2} {3} {4}'.format(tokens[4], tokens[0], tokens[1], tokens[2], tokens[3]))