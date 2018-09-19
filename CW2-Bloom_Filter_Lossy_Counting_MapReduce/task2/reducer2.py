#!/usr/bin/python
import sys

count = 1

for line in sys.stdin:
	line = line.strip().split()
	if count <= 10:
		print('{0} {1}'.format(line[0], line[1]))
		count += 1