#!/usr/bin/python

import sys

for line in sys.stdin:
	line = line.strip().split()
	print('{0} {1} {2}\t{3}'.format(line[0], line[1], line[2], line[4]))