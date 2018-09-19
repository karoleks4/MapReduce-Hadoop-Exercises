#!/usr/bin/python
import sys
import os

for line in sys.stdin:
	tokens = line.strip().split()
	file  = os.path.basename(os.environ["mapreduce_map_input_file"])
	for token in tokens:
		print('{0}\t{1} {2}'.format(token, file, 1))