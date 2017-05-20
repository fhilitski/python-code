import sys, datetime

def get_fine(ret, due):
	fine = -1
	ret_date = datetime.date(ret[2], ret[1], ret[0])		
	due_date = datetime.date(due[2], due[1], due[0])		
	if (ret_date <= due_date):
		fine = 0
	else: 	
		diff = ret_date - due_date
		if (ret_date.year == due_date.year):
			if (ret_date.month == due_date.month):
				fine = 15 * diff.days
			else:
				fine = 500 * abs(ret_date.month - due_date.month)
		else:
			fine = 10000
	return fine
				

#initial info on startup
print("First input - 3 space sep integers: day month year of return ")
print("Next line - day month year due") 
return_date=list(map(int,input().split(' ')))
due_date=list(map(int,input().split(' ')))

print(get_fine(return_date, due_date))




# for i in range(T):
#    data=int(input()) #this is an integer to test
#    print(create_output(test_prime(data)))
	
