def topost(infix):
	precedence={}
	precedence['+']=1
	precedence['-']=1
	precedence['*']=2
	precedence['/']=2
	res=[]
	op=[]	
	for c in infix:
		if c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or c.isdigit():
			res.append(c)
		else:
			while(len(op)>0 and precedence[c]<=op[-1]):			

				print "len(op),c,precedence[c],op[-1]"
				print len(op),c,precedence[c],op[-1]
				res.append(op.pop())
			op.append(c)
	
	while(len(op)>0):
		res.append(op.pop())		
	return res

infix="A*B+C*D"
print topost(infix)