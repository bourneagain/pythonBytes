#'*4+23' or '423+*' in prefix and postfix notation respectively.

def topost(infix):
	res=[]
	op=[]	
	for c in infix:
		if c.isdigit():
			res.append(c)
		else:
			while len(op) > 0 and op[len(op)-1] in ['*','/'] and c in ['+','-']: 
				res.append(op.pop())
			op.append(c)
	while(len(op)>0):
		res.append(op.pop())
	return res

infix="4+5*2"
print topost(infix)
