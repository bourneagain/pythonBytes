import pprint
def lisub(a):
	lis={}
	prev={}

	lis[0]=1
	prev[0]=-1
	maxl=1
	best=0

	seq=[]
	for i in range(1,len(a)):
		lis[i]=1
		prev[i]=-1
	#	print "------------"
		for j in range(i,-1,-1):
	#		print "i:",i,a[i],"j:",j,a[j]
			if lis[j]+1 > lis[i] and a[j] < a[i]:
				lis[i] = lis[j] + 1
				prev[i]=j
	#			print "added a[j] < a[i]",a[j],a[i]
		if lis[i] > maxl:
			maxl = i
			best=i	

	#print best,maxl,prev
	pprint.pprint(prev)
	


a=[3, 2, 6, 4, 5, 1]
lisub(a)
"""

[3, 2, 6, 4, 5, 1]
------------
------------
i: 1 2 j: 0 3
------------
i: 2 6 j: 0 3
added a[j] < a[i] 3 6
i: 2 6 j: 1 2
------------
i: 3 4 j: 0 3
added a[j] < a[i] 3 4
i: 3 4 j: 1 2
i: 3 4 j: 2 6
------------
i: 4 5 j: 0 3
added a[j] < a[i] 3 5
i: 4 5 j: 1 2
i: 4 5 j: 2 6
i: 4 5 j: 3 4
added a[j] < a[i] 4 5
------------
i: 5 1 j: 0 3
i: 5 1 j: 1 2
i: 5 1 j: 2 6
i: 5 1 j: 3 4
i: 5 1 j: 4 5
(1, [6, 4, 5, 5])
"""
