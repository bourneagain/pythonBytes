# you can use print for debugging purposes, e.g.
# print "this is a debug message"
def findGap(minA,maxA,A):
	minGapList=[]
	entireMax=[]
	for i in range(minA,maxA+1,1):
		for el in A:
			print el
			addEle=abs(el-i)
			print addEle
		 	minGapList.append(addEle)
		print "MIN IS " + str(min(minGapList))
		entireMax.append(min(minGapList))
		print "ENTIER MAX "
		print max(entireMax)
		minGapList=[]
		
def solution(A):
    # write your code in Python 2.7
    minA=min(A)
    maxA=max(A)
    findGap(minA,maxA,A)
    pass


A=[10,0,8,2,-1,12,11,3]
solution(A)
