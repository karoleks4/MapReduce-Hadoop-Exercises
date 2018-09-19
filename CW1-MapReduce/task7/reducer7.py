#!/usr/bin/python3

import sys

now = None
total = ""

for line in sys.stdin:
	now = line.strip().split()

	if (now[1] == "mark"):
		total = total + " (" + now[3] + "," + now[2] + ")" 
	elif (now[1] == "student"):
		total = now[0] + " -->" + total
		print(total)
		total = ""