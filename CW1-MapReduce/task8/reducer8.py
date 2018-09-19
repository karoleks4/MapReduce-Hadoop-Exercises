#!/usr/bin/python

import sys

total = 0
min_avg = 101
idx = []

for line in sys.stdin:
	line = line.strip().split()
	for n in range(2, len(line)):
		total += float(line[n][2:-2].split(',')[0])
	avg = total/(len(line) - 2)
	
	if avg == min_avg:
		idx.append(int(line[0][2:-2]))
	if avg < min_avg:
		min_avg = avg
		idx = []
		idx.append(int(line[0][2:-2]))
	total = 0

if len(idx) == 1:
	print('names: {0} scores: {1}'.format(idx[0], min_avg))
else:
	print('names: {0} scores: {1}'.format(idx, min_avg))