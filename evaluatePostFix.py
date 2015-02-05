def evalPost(a):
	res=[]

	for n in a:
		if n.isdigit():
			res.append(n)
		else:
			try:
				a=res.pop()
				b=res.pop()
			except:
				print "error in key"
			res.append(cal(int(b),int(a),n))
	return res.pop()


def cal(a,b,op):
	if op == '*':
		return a*b
	elif op == '+':
		return a+b
	elif op == '-':
		return a-b
	else:
		try:
			return a/b
		except:
			print "divide by zero"


a=['2','3','4','+','*']
a=['2','3','*','5','2','*','+']
#a=-+*23*549
a=['9','4','5','*','3','2','*','+','-']
print evalPost(a)


