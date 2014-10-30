
def sumList(aList):
		sum=0
		print "PRINT ALIST " + aList
		for i in aList:
			print "inside sumList i" + str(i)
			sum+=i
		return sum

def sumRow(numRow,numColumn,matrix):
	rowSum=0
	for i in range(numRow):
		print "printing i " + str(i)
		rowSum=sumList(i[0])+int(rowSum)
	totalSum=rowSum
	print totalSum

def solution(A):
	# write your code in Python 2.7
	numRow=len(A)
	num=len(A[0])
	print numRow
	print num
	#sumRow(5,5,A)
	pass

A= [[0 for x in xrange(5)] for x in xrange(5)] 
A[1][0]=3
A[0][0]=2
solution(A)
