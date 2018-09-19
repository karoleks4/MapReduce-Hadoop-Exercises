#!/usr/bin/python3

import sys
import math

prev = None
now = None
counts = []
count = 0
total = 0.0
en = 0.0

for line in sys.stdin:
	now = line.strip().split()

	if prev == None:
		pass
	elif (now[0] == prev[0]) & (now[1] == prev[1]) & (now[2] == prev[2]):
		count = float(prev[3])
		counts.append(count)
		total += count
	else:
		count = float(prev[3])
		counts.append(count)
		total += count
		for i in range(len(counts)):
			en -= (counts[i] / total) * (math.log(counts[i] / total, 2))
		print('{0} {1} {2} {3}'.format(prev[0], prev[1], prev[2], en))
		en = 0.0
		total = 0
		counts = []
	prev = now
	
if (prev):
	print('{0} {1} {2} {3}'.format(prev[0], prev[1], prev[2], en))