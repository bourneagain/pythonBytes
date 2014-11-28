def compress(A):
	#a a b c c c c c a a a
	counter=1;
	opstring=[]
	for i in range(0,len(A)-1):
		if A[i] == A[i+1]:
			counter+=1
		else:
			opstring.append(A[i])
			opstring.append(counter)
			counter=1	
	if counter!=1:
		opstring.append(A[i-1])
		opstring.append(counter)
		
	print opstring	

compress("aabcccccaaa")
