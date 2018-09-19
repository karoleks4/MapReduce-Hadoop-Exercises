#!/usr/bin/python

import sys

for line in sys.stdin:
	line = line.strip().split()
	if line[0] == "student":
		print('{0}\t{1}\t{2}'.format(line[1], line[0], line[2]))
	elif line[0] == "mark":
		print('{0}\t{1}\t{2} {3}'.format(line[1], line[0], line[2], line[3]))