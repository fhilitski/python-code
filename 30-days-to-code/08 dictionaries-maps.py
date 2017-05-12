import sys

n = int(input().strip())
#num of entries
#phone book
pb = dict()

#read input phonebook
for i in range(n):
	name, num = input().strip().split(' ')
	pb[name] = int(num)

#read unknown num of queries
query = input().strip()
while (query != ''):
	if query not in pb:
		print('Not found')
	else:
		print('{}={}'.format(query, pb[query]))
	query = input().strip()	
	
#the last part can also be accomplished as 
#lines = sys.stdin.readlines()
#for i in lines:
#    name = i.strip()
#    if name in pb:
#        print(name + '=' + str( pb[name] ))
#    else:
#        print('Not found')