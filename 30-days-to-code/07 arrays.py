#python3
#
import sys

n = int(input().strip())
a = [int(num_in) for num_in in input().strip().split(' ')]

a.reverse()
s_out = ''
for i in range(n):
	s_out += str(a[i]) + ' '
	
print(s_out)
