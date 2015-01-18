def changeString(string, src_list):
	string = list(string)
	src = list(src_list)
	check={}
	for i in src_list:
		check[i]=True

	p1=0	
	p2=0
	while p1 < len(string):
		if string[p1] not in check:
			p1+=1
			p2+=1
		else:
			p1+=1
			string[p2] = string[p1]

	return string[:p2]

print changeString('shyam','ha')

