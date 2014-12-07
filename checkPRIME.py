def checkprime(n):
	if n<=1:
		return -1
	if n==2:
		return 1
	for i in range(2,n/2):
		if(n%2==0):	
			return -1
	return 1

print checkprime(99991923912391923912)

		