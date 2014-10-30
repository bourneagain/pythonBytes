alist=[]
def printTwo(n,max):
	global alist
	newNum=n*10
	newMax=(n+1)*10
	for i in range(newNum,newMax,1):
		if ( i <= max): alist.append(i)

def printSort(N):
	global alist
	for i in range(N):
		alist.append(i)
		printTwo(i,N)	
		if alist[-1] >= N:
			break

printSort(50)
print alist
