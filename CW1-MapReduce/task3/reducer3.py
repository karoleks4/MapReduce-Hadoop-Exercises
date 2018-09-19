#!/usr/bin/python
import sys

max_bytes = 0
max_tokens = 0

for line in sys.stdin:
	line = line.strip()
	curr_bytes = len(line)
	curr_tokens = len(line.split())

	if curr_bytes > max_bytes:
		max_bytes = curr_bytes
	if  curr_tokens > max_tokens:
		max_tokens = curr_tokens

print('{0}\t{1}'.format(max_bytes, max_tokens))