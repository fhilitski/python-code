#!/bin/python3

import sys


n = int(input().strip())
a = [int(a_temp) for a_temp in input().strip().split(' ')]
swaps = 0
for j in reversed(range(n)):
	for i in range(j):
		if a[i]>a[i+1]:
			tmp = a[i+1]
			a[i+1] = a[i]
			a[i] = tmp
			swaps += 1

print('Array is sorted in {} swaps.'.format(swaps))
print('First Element: {}'.format(a[0]))
print('Last Element: {}'.format(a[n-1]))