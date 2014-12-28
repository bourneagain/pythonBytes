import math
def checkprime(n):
	if n<=1:
		return -1
	if n==2:
		return 1
	for current in range(3, int(math.sqrt(n) + 1), 2):
		if n % current == 0: 
			return False
	return True

print checkprime(7)

		
