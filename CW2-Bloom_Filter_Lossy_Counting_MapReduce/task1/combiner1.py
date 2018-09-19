#!/usr/bin/python
import sys

total = 0
now = None
prev = '  '

for line in sys.stdin:
	now = line.strip().split()
	if (prev[0] == now[0]) & (prev[1] == now[1]):
		total +=  1
	elif (prev[0] == now[0]) & (prev[1] != now[1]):
		print('{0} {1} {2}'.format(prev[0], prev[1], total))
		prev = now
		total = 1
	else:
		if (prev != '  '):
			print('{0} {1} {2}'.format(prev[0], prev[1], total))
		prev = now
		total = 1
print('{0} {1}\t{2}'.format(now[0], now[1], total))