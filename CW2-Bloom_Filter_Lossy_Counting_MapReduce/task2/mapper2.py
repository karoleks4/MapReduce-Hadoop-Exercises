#!/usr/bin/python
import sys
import xml.etree.ElementTree as ET
from heapq import heappushpop, heappush, heappop

recs = []

for line in sys.stdin:
	line = line.strip()
	content = ET.fromstring(line)
	if content.attrib['PostTypeId'] == '1':
		post_id = content.attrib['Id']
		count = content.attrib['ViewCount']
		if len(recs) == 10:
			heappushpop(recs,[int(count), post_id])
		else:
			heappush(recs,[int(count), post_id])

for r in recs:
	print('{0}\t{1}'.format(r[0], r[1]))