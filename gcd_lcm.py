def gcd(a,b):
	while a!=b:
		if a > b:
			a = a-b
		else:
			b = b-a
	return a

def lcm(a,b):
	m=max(a,b)
	while True:
		if m%a == 0 and m%b == 0:
			return m
		else:
			m+=1

print lcm(30,45)


