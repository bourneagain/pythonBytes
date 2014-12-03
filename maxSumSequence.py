def maxSum(A):
	runningSum=0
	finalSum=0
	res=[]
	for i in A:
		if i+runningSum > 0:
			runningSum+=i
			res.append(i)
		else:
			runningSum=0
			res=[]
		finalSum=max(finalSum,runningSum)
		print i
		print "RUNNING",
		print runningSum,
		print "FINAL",
		print finalSum	
		print "----"
	print res
	print finalSum



A=[5,-9,6,-2,3]

#5,-9,6,-2,3
#5,8,-1,5,3,6

maxSum(A)