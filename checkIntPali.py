def ispali(n):
	#1221
	digits = countDigits(n)
	div  = 10**(digits-1)
	while n!=0:
		print n
		r = n/div
		l = n%10
		if l != r:
			return False
		else:
			n = (n%div)/10
			div = div/100
	return True			


def countDigits(n):
	i = 0
	while  n > 0:
		i+=1
		n=n//10
	return i

print ispali(123321)	