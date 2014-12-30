def isU(str):
	checker=0;
	if len(str) > 256:
		return False
	for c in str:
		val = ord(c) - ord('a')
		if checker & ( 1 << val ) > 0:
			return False
		else:
			checker |= ( 1 << val )  
	return True

print isU("sama")
