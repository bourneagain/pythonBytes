import sys
numArray={}
def clearNum(i,n):
	global numArray;
	a=i
	print "ENTERING FOR " + str(i)
	loopCount=0;
	while(i<n):
		if loopCount == 0:
			loopCount=1
			print "CONTINUE FOR ONCE"
			print "i:" + str(i)
			i=i+a
		else:
			numArray[i]=-1
			print "i:" + str(i) + "=="+str(numArray[i])
			i=i+a
		

def arrayprime(n):
	for i in range(2,n):
		clearNum(i,n)
	print numArray.keys()
sys,n=sys.argv
n=int(n)
arrayprime(n)
	
for i in range(n):
	if i not in numArray.keys():
		print i


