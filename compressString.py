def compress(string):
	#c a a
	if len(string) == 0 or len(string) == 1:
		return string
	prev=string[0]
	strc=1
	newStr=[]
	for i in range(1,len(string)):
		if string[i] == prev:
			strc+=1
		else:
			newStr.append(prev)
			newStr.append(strc)
			strc=1
		prev=string[i]
	newStr.append(prev)
	newStr.append(strc)
	newStr=map(lambda x: str(x),newStr)	
	newStr=''.join(newStr)	
	
	if len(newStr) > len(string):
		return string
	else:
		return newStr

print compress("saaaaaaaaaaaaaaaaaaammmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmaaaa")	
