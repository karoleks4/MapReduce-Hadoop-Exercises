#!/usr/bin/python3
import sys

prev = None
total = 0

for line in sys.stdin:
	now = line.strip()
	count = 1

	if (prev == now):
		total += count
	elif (prev != now) & (total == 0) & (prev != None):
		print(prev)
	else:
		total = 0
	prev = now

if total == 0:
	print(now)