def infixtopost(a):
	postfix=[]
	op=[]
	for token in a:
		print token+" ---- ",
		if token in "abcdefghijklmnopqrstuvwxyz" or token in "0123456789":
			postfix.append(token)
		elif token == '(':
			op.append(token)
		elif token == ')':
			while op[-1] != '(':
				postfix.append(op.pop())
		else:
			if len(op) == 0:
				op.append(token)
			else:
				while len(op) and checkOperatorPrecedence(op[-1],token):
					postfix.append(op.pop())
				if len(op):
					op.append(token)
		print ' '.join(postfix),":",' '.join(op),"          "
	
	return ' '.join(postfix)


def checkOperatorPrecedence(a,b):
	"""
	0 if a's precedence is more than b operator
	1 otherwise
	"""
	check={}
	check['(']=3
	check['^']=2
	check['*']=2
	check['/']=2
	check['-']=1
	check['+']=1
	if check[a] <= check[b]:
		return 1
	else:
		return 0


infix="(a+b)*(c+d)"
#infix="a+b*(c^d-e)^(f+g*h)-i"

print infixtopost(infix)
