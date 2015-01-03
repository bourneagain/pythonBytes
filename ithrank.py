import random
def ith_rank(a,rank):
	if rank > len(a):
		return False
	pivot_index=random.randint(0,len(a)-1)
	print "---",rank,a,a[pivot_index]
	left=[]
	right=[]
	pivot=[]
	for i in a:
		if i < a[pivot_index]:
			left.append(i)
		else:
			#pivot.append(i)
			right.append(i)
	# print "LEFT:",left
	# print "RIGHT:",right
	if len(left) == rank:
		return max(left)
	if len(left) > rank:
		return ith_rank(left,rank)
	else:
		#print "RIGHT:",right
		return ith_rank(right,rank-len(left))

A=[3,2,1,4,6,7,-1,2]
print ith_rank(A,10)

