#for prefix expression evalution : same as postfix 
#just reverse and use the same : only in / and - use a and b the other way that not a-b but b-a 
def evalPost(postfix):
	res=[]
	op=[]
	for i in postfix:
		if i.isdigit():
			print "entering " + str(i)
			res.append(i)
		else:
			print "entering operator" + str(i)
			op.append(i)
			print "len of op"  + str(len(op))
			if  len(op) > 0:
				print "popping"
				b=int(res.pop())
				a=int(res.pop())
				print a,b
				if i=="*": c=int(a*b)
				if i=="+": c=int(a+b)
				if i=="-": c=int(a-b)
				print c
				res.append(c)	
	return res,op

def evalPre(prefix):
	prefixList=[]
	for i in prefix:
		prefixList.append(i)
	prefixList.reverse()
	print prefixList
	return evalPost(prefixList)

#https://www.youtube.com/watch?v=MeRb_1bddWg

postfix="23*52*+"
prefix="-+*23*549"
print evalPost(postfix)
#print evalPre(prefix)
#5 2
#10
#3 10
#13
#['2', 13]
