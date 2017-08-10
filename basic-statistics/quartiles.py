#!/usr/local/bin/python3

import mystat

# start main section
# inputs
n = int(input())
x_in = [int(in_temp) for in_temp in input().strip().split()]

# output stdout
for i in mystat.quartile(x_in,0): print(i)
