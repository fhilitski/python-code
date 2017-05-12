#!/bin/python3
import sys

def hourglass_sum(array,i_s,j_s):
	#i,j are stating indexes
	sum = 0
	for i in range(i_s, i_s+3):
		for j in range(j_s, j_s+3):
			sum += array[i][j]
	
	sum -= array[i_s+1][j_s]
	sum -= array[i_s+1][j_s+2]
	return sum
	

arr = []
for arr_i in range(6):
   arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
   arr.append(arr_t)

m = hourglass_sum(arr,0,0)
for i in range(4):
	for j in range(4):
		m = max(m,hourglass_sum(arr,i,j))
print(m)