#python3 
#
t = int(input().strip())
for i in range(t):
	s = input().strip()
	seven = ''
	sodd = ''
	for j in range(len(s)):
		if (j%2 == 0):
			seven += s[j]
		else:
			sodd += s[j]
	print(seven+' '+sodd)
	
