#!/usr/bin/python
import sys
import xml.etree.ElementTree as ET

for line in sys.stdin:
	line = line.strip()
	content = ET.fromstring(line)
	#Question (AcceptedAnswerId, Id):
	if content.attrib['PostTypeId'] == '1': 
		if 'AcceptedAnswerId' in content.attrib:
			print('{0}\t{1}'.format(content.attrib['AcceptedAnswerId'], content.attrib['Id']))
	#Answer (Id, OwnerUserId, Flag):
	else:
		print('{0}\t{1} {2}'.format(content.attrib['Id'], content.attrib['OwnerUserId'], 1))