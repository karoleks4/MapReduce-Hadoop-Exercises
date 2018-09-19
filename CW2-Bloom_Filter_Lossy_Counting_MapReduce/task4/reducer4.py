#!/usr/bin/python
import sys
import random

line_sum = -1
resevoir = None

for line in sys.stdin:
	line = line.strip().split('\t')
	line_sum += int(line[1])
	if random.randint(0, line_sum) < int(line[1]):
		resevoir = line[0]
print(resevoir)