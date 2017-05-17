import sys, math

def test_prime(num):
	if num == 1:
		result = False #by definition 1 is not prime
	else:
		rem = 1
		test_num = 1
		prime_flag = False
		while rem != 0:
			test_num = test_num + 1
			rem = num % test_num
			if test_num > math.sqrt(num):
				prime_flag = True	
				break
	
		result = (test_num == num) or prime_flag
	return result

def create_output(test_result):
	return "Prime" if test_result else "Not prime"

#initial info on startup
print("First input - number of test cases (int T)")
print("subsequent T inputs - actual test cases") 
T=int(input())

for i in range(T):
    data=int(input()) #this is an integer to test
    print(create_output(test_prime(data)))
	
