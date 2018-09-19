#!/usr/bin/python
import sys

now = None
prev = ' '

for line in sys.stdin:
	now = line.strip().split()
	#AcceptedAnswerId == Id
	if prev[0] == now[0]:
		#Look for the flag and return OwnerUserId, Id (from the question)
		if len(prev) == 3:
			print('{0} {1}'.format(prev[1],now[1]))
		elif len(now) == 3:
			print('{0} {1}'.format(now[1],prev[1]))
	prev = now