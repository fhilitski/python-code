#!/bin/python3
class Difference:
	def __init__(self, a):
		self.__elements = a
		
	def computeDifference(self):
		max_diff = -1
		a = self.__elements
		for i in range(len(a)):
			for j in range(i):
				diff = abs(a[i] - a[j])
				max_diff = max(max_diff, diff)
		self.maximumDifference = max_diff
		
# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)