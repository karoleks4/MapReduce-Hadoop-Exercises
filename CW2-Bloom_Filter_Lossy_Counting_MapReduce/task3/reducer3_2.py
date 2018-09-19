#!/usr/bin/python
import sys

now = None
prev = ' '
docs_max = ''
user_max = ''
count_max = 0
docs = ''
count = 0

for line in sys.stdin:
	now = line.strip().split()
	if prev[0] == now[0]:
		docs += ' ' + prev[1] + ','
		count += 1
	elif prev[0] != now[0] and prev[0] != ' ':
		docs += ' ' + prev[1] + ','
		count += 1
		if count_max < count:
			count_max = count
			docs_max = docs
			user_max = prev[0]
		count = 0
		docs = ''
	prev = now
if prev[0] == now[0]:
		docs += ' ' + prev[1] + ','
		count += 1
if count_max < count:
	count_max = count
	docs_max = docs
	user_max = prev[0]

print('{0} ->{1}'.format(user_max,docs_max[:-1]))