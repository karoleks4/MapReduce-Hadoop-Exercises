#!/usr/bin/python
import sys

for line in sys.stdin:
	line = line.strip().split()
	print('{0}\t{1}'.format(line[0], line[1]))