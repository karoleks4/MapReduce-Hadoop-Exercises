#!/usr/bin/python
import sys
import math
import mmh3
import bitstring

class BloomFilter:
	def __init__(self, size, num_hashes, ran):
		self.ran = ran
		self.num_hashes = num_hashes
		self.size = size / self.num_hashes
		self.filter = bitstring.BitArray(self.size)
		self.num_hashes = 1

	def insert(self, key):
		loc = mmh3.hash(key, self.ran) % self.size
		self.filter[loc] = 1

	def query(self, key):
		loc = mmh3.hash(key, self.ran) % self.size
		if self.filter[loc] == 0:
			return False
		return True

ran = 2
n = 1897987
p = 0.009
m = int(math.ceil(-((n * math.log(p)) / (math.log(2) ** 2))))
k = int(round((m * math.log(2)) / n))
bloom = BloomFilter(m, k, ran)

for line in sys.stdin:
	line = line.strip()
	if bloom.query(line) == False:
		bloom.insert(line)
		print(line)
