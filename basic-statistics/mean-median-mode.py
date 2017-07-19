#!/usr/local/bin/python3.5

def mean(array_in):
	result = sum(array_in)/len(array_in)
	return result

def median(array_in):
	result = 0
	sorted_in = array_in
	sorted_in.sort()
	l = len(sorted_in)
	if l%2 == 1:
		#the number of elements is odd
		#find the middle element
		index_median = int((l-1)/2)
		result = array_in[index_median]
	else:
		index_median = int(l/2)
		result = (sorted_in[index_median] + sorted_in[index_median - 1])/2
	return result

def mode(array_in):
	unique_in = set(array_in)
	n_unique = len(unique_in)
	count = [0 for i in range(n_unique)]
	
	for val in array_in:
		i = unique_in.index(val)
		count[i] = count[i] + 1

	max_count = array_in[count.max()]
	return array_in[count.max()]

	
		
			
	
	

N = int(input('Total numbers N: '))
# numbers_in = map(int, input('N space separated integers: ').split(" "))
n_in = [int(a_temp) for a_temp in input('N space-separated integers: ').strip().split()]

#print(N)
#print(numbers_in)
#print(n_in)

print(mean(n_in))
print(median(n_in))
print(mode(n_in))
