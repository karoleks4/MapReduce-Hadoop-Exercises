#!/usr/bin/python3
import sys

prev = None
now = None
total = 0

for line in sys.stdin:
	now = line.strip()

	if (prev == now):
		total += 1
	elif (prev != now) & (prev != None):
		total += 1
		print(prev, total, sep='\t')
		total = 0
	prev = now

if prev == now:
	total += 1
	print(prev, total, sep='\t')