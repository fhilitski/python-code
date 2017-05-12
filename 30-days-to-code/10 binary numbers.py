#!/bin/python3
import sys


n = int(input().strip())
nbs = "{:b}".format(n)
s = nbs.split('0')
l = 0
for i in range(len(s)):
	l = max(len(s[i]), l)
print(l)
	

