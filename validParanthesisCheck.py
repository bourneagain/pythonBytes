def validParant(S):
	op=[]
	for i in S:
		if i in ['{','(','[']:
			op.append(i)
		else:
			t=op[-1]
			if i == '}' and t != '{':
				return False
			elif i == ']' and t != '[':
				return False
			elif i == '}' and t != '{':
				return False
	return True

print validParant('({[]]})')


