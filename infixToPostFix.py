def infixtopost(a):
	postfixList=[]
	opStack=[]
	prec = {}
	prec["*"] = 3
	prec["/"] = 3
	prec["+"] = 2
	prec["-"] = 2
	prec["("] = 1
	for token   in  a:
		if  token   in  "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"  or  token   in  "0123456789":
			postfixList.append(token)
		elif    token   ==  '(':
			opStack.append(token)
		elif    token   ==  ')':
			topToken    =   opStack.pop()
			while   topToken    !=  '(':
				postfixList.append(topToken)
				topToken    =   opStack.pop()
		else:
			while len(opStack) and (prec[opStack[-1]] >= prec[token]):
				postfixList.append(opStack.pop())
			opStack.append(token)

	while len(opStack):
		postfixList.append(opStack.pop())
	return  "   ".join(postfixList)

def checkOperatorPrecedence(a,b):
	"""
	0 if a's precedence is more than b operator
	1 otherwise
	"""
	check={}
	check['(']=1
	check['*']=2
	check['/']=2
	check['-']=3
	check['+']=3
	if check[a] <= check[b]:
		return 1
	else:
		return 0


infix="(a+b)*(c+d)"
infix='5*3^(4-2)'
infix='(2+3)*9/'

infix="(A+B)*C-(D-E)*(F+G)"
infix="a+b*ac*d"
#infix="a+b*(c^d-e)^(f+g*h)-i"

print infixtopost(infix)
