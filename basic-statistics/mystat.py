#--------------------------------
# Statistical functions		|
#--------------------------------
# mystat.py			|
#--------------------------------

import math

# calculating mean of the array_in
def mean(array_in):
	result = sum(array_in)/len(array_in)
	return result

# calculating median of the array_in
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


# calculating mode of the array_in
def mode(array_in):
	unique_in = set(array_in)
	n_unique = len(unique_in)
	count = 0
	mode = array_in[0]
	for i in unique_in:
		this_count = array_in.count(i)
		if this_count > count:
			count = this_count
			mode = i
		elif (this_count == count):
			mode = mode if (mode < i) else i
	return mode

# calculating weighted mean of values values_in with weights_in
def weighted_mean(values_in, weights_in):
	vw = [v*w for v,w in zip(values_in, weights_in)]
	sum_vw = sum(vw);
	sum_w = sum(weights_in)
	return sum_vw/sum_w

# calculation of standard deviation of the values in values_in list
def standard_deviation(values_in):
	mu = mean(values_in)
	dev2 = sum([(val - mu)**2 for val in values_in])
	sigma2 = dev2 / len(values_in)
	return math.sqrt(sigma2)

# calculating quartile q_in of the values in values_in list
# q_in can be 1, 2, 3
#The quartiles of an ordered data set slit the data set into  equal groups:
# Q1 =  middle number between the smallest number in a data set and its median.
# Q2 = the median ( percentile) of the data set.
# Q3 = middle number between a data set's median and its largest number.
def quartile(values_in, q_in):
	sorted_in = values_in
	sorted_in.sort()

	l = len(values_in)

	q2 = median(sorted_in)
	if l%2 == 1:
		index_q2 = sorted_in.index(q2)
		bottom_index = index_q2
		top_index = index_q2+1
	else:	
		index_q2 = int(l/2)
		top_index = index_q2
		bottom_index = index_q2
	
	q1 = median(sorted_in[:bottom_index])
	q3 = median(sorted_in[top_index:])
	return [q1, q2, q3]

#-------------------------------------------
#|  end function defs                      |
#-------------------------------------------
