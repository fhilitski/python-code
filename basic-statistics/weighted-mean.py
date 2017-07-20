#!/usr/local/bin/python3

import mystat

# start main section
# inputs
n = int(input())
x_in = [int(in_temp) for in_temp in input().strip().split()]
w_in = [int(in_temp) for in_temp in input().strip().split()]

# output stdout
print("{:.1f}".format(mystat.weighted_mean(x_in, w_in)));
