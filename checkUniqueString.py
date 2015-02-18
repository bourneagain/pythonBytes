def checkUniq(st):
	if len(st) > 256:
		return False
	check = 0
	#boolval=[False]*26
	for i in st:
		n = ord(i)-97
		if check & (1<<n) :
			return False
		else:
			check |= check + (1<<n)

	return True			

print checkUniq('sam')