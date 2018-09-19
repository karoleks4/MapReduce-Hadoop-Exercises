#!/usr/bin/python
import sys
import random

resevoir = []
line_number = 0

for line in sys.stdin:
	line = line.strip()
	if len(resevoir) < 100:
		resevoir.append(line)
	else:
		i = random.randint(0, line_number)
		if i < 100:
			resevoir[i] = line
	line_number += 1

for i in range(0,len(resevoir)):
	print(resevoir[i])