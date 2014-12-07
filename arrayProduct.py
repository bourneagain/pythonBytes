def sol(A):
	# p to store the product of array A
	p=1;
	for i in A:
		p=p*i
	print p
	# p now contains the array product

	# creating a new array to output with same length l
	outputList=[]
	count=0
	# have a loop to iterate l(A) 
	for j in A:
		# what if there is a 0 ?
		# avoid the divide by zero error; while trying to get the p/A[count]
		if A[count] == 0 :	
			print "PRINTING"
			print A[:count]
			print A[count+1:]
			print "PRINTING"
			outputList.append(p)
		else:
			outputList.append(p/A[count])
		count=count+1

	print outputList

A=[1,3,0,5,6,4]
print A
sol(A)
