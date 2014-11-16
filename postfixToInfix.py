def postFixToInfix(A):
	res=[]
	temp=[]
	for i in A:
		if i in "abcdefghijklmnopqrstuvwxyz" or i.isdigit(): 
			res.append(i)
		else:
			if(len(res)<2):
				print "ERROR"
			else:
				t=""
				b=res.pop()
				a=res.pop()
				t="("+a+""+i+""+b
				res.append(t)
	return res	
A="abc-+de-fg-h+/*"
print postFixToInfix(A)


#['((a+(b-c))*((d-e)/((f-g)+h)))']
