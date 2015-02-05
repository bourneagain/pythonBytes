import time,sys
def findDup(A):
	if len(A) < 1:
		raise Exception("len < 1 ")
	for i in range(0,len(A)):
		if A[i]<i:
			print "dup is " + str(A[i])
		while A[i] != i :
				print "     swapping" ,
				print A[i],A[A[i]]
#A[i],A[A[i]]=swap(A[i],A[A[i]])
				x,y=swap(A[i],A[A[i]])
				print x
				A[i]=x
				print A[i]
				print y
				A[A[i]]=y
				print A[A[i]] 
				sys.exit()
				A[A[i]]=y
				print x,y,
				print "DONE",
				print A[i],A[A[i]]
				time.sleep(2)
		


def swap(a,b):
	print "INSIDE FUNC"
	print a,b
	a=a^b
	b=b^a
	a=a^b
	print a,b
	return a,b
A=[2,1,0]
findDup(A)
