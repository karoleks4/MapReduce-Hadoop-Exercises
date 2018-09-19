#!/usr/bin/python3
import sys

for line in sys.stdin:
	tokens = line.strip().split()
	if len(tokens) >= 4:
		for idx in range(len(tokens) - 3):
			print('{0} {1} {2} {3}'.format(tokens[idx], tokens[idx+1], tokens[idx+2], tokens[idx+3]))