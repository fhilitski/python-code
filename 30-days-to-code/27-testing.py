import sys, random 
#all n values have to be unique
all_n = set([0])


#first, generate t
t = 5#random.randint(1,9)
print(t)
for i in range(t): 
	#generate each test case
	#start with n k
	n = 0
	while (n in all_n):
		n = random.randint(3,200)
	all_n.add(n)
	k = random.randint(1,n)
	print(*[n,k])
	a = [0]
	#now generate the arrival times
	for j in range(n-1):
		a.append(random.randint(-1000, 1000))
	print(*a)

