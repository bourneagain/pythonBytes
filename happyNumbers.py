def check_happyNumbers(x):
	aset = set()
	while True:
		s = sum(int(i)**2 for i in str(x))
		if s in aset:
			return False
		elif s == 1:
			return True
		else:
			# aset = aset | {s}
			aset.add(s)
			x=s

print check_happyNumbers(20)