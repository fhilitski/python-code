import sys, math

def test_prime(num):
	if num == 1:
		result = False #by definition 1 is not prime
	else:
		rem = 1
		test_num = 1
		while rem != 0:
			test_num = test_num + 1
			rem = num % test_num
			if test_num > math.sqrt(num):
				break
			
		result = (test_num == num)
	
	return result

def create_output(test_result):
	return "Prime" if test_result else "Not prime"

T=int(input())

for i in range(T):
    data=int(input()) #this is an integer to test
    print(create_output(test_prime(data)))
	