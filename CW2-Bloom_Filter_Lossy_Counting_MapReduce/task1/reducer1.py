#!/usr/bin/python
import sys

total_file = 0
total = 0
now = None
prev = '  '
doc_val = '{'

for line in sys.stdin:
	now = line.strip().split()

	if (prev[0] == now[0]) & (prev[1] == now[1]):
		total +=  int(prev[2])
	elif (prev[0] == now[0]) & (prev[1] != now[1]):
		doc_val += '(' + prev[1] + ', ' + str(total) + '), '
		total_file += 1
		prev = now
		total = int(now[2])
	else:
		if prev != '  ':
			doc_val += '(' + prev[1] + ', ' + str(total) + ')}'
			total_file += 1
			print('{0} : {1} : {2}'.format(prev[0], total_file, doc_val))
		prev = now
		total = int(now[2])
		doc_val = '{'
		total_file = 0

doc_val += '(' + prev[1] + ', ' + str(total) + ')}'
total_file += 1
print('{0} : {1} : {2}'.format(prev[0], total_file, doc_val))