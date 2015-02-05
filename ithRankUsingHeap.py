import heapq
import random
def ithRank(a,k):
	a=map(lambda x: -1*x, a)
	l=a[:k+1]
	heapq.heapify(l)
	for i in a:
		heapq.heappushpop(l,i)

	return heapq.heappop(l)

A=[3,2,1,4,6,7,-1,2]
print ithRank(A,2)
