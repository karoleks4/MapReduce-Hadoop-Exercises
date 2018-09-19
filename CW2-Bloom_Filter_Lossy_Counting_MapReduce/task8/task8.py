#!/usr/bin/python
import sys
import math

n = 0
s = 0.01
e = 0.001
window_size = math.ceil(1/e)
counters = {}

for line in sys.stdin:
	line = line.strip()
	n += 1
	if line in counters:
		counters[line] += 1
	else:
		counters[line] = 1

	if n % window_size == 0:
		for l, f in counters.items():
			if f == 1:
				del counters[l]
			else:
				counters[l] -= 1

for l in counters:
	if counters[l] >= (s - e) * n:
		print(l)