def factorialZero(n):
	s = 0
	i = 1
	while n/5**i > 0:
		s+=n/5**i
		i+=1
	return s
print factorialZero(100)