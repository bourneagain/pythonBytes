def add(a,b):
	return a+b

def mult(a,b):
	if a==0 or b==0:
		return 0
	count=1;
	result=0;
	while count<=abs(b):
		print count
		result+=a
		count+=1
	if(b<0):
		return neg(result)
	else:
		return result

def subt(a,b):
	return a+neg(b)

def divide(a,b):
	if b==0:
		raise Exception("divide by zero")

	#a/b=x
	#a=bx
	c=abs(b)
	result=0
	while(c<=abs(a)):
		result+=1
		c+=abs(b)
	if ( a>0 and b>0 ) or ( a<0 and b<0 ):
		return result
	else:
		return neg(result)


def neg(n):
	neg=0
	if n>0:
		flag=-1
	else:
		flag=1

	result=0
	while(n!=0):
		result+=flag
		n+=flag

	return result

print divide(16,-8)
#print subt(-2,-3)