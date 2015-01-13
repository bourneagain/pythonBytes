def lisSub(A):
	l=[]
	l.append(A[0])
	lis=[1]*len(A)

	for i in range(1,len(A)):
		for j in range(0,i):
			#for every value before i, check if they are smaller than i 
			# if so check if adding one to the list at that position makes it longer than 
			#what can be got for lis at i
			
			if A[i] > A[j] and lis[j] + 1 > lis[i]:
				lis[i] = lis[j] + 1
				if l[-1] < A[i]:
					l.append(A[i])
	return max(lis),l
	



			#lis[i]=max(lis[i] for i in lis.keys() if all(x>A[i] for x in A[:i]))
			#print lis[i]


# def longest_increasing_subsequence(d):
#     'Return one of the L.I.S. of list d'
#     l = []
	
#     for i in range(len(d)):
#     	for j in range(i):
#     		if l[j][-1] < d[i]:
#     			pass
# 		# a=max( [ l[j] for j in range(i) if l[j][-1] < d[i] ] or [ [] ], key=len)
# 		# print a
# 		# l.append( max( [l[j] for j in range(i) if l[j][-1] < d[i]] or [[]], key=len)+ [d[i]])
		
#     return max(l, key=len)

A=[10, 22, 9, 33, 21, 50, 41, 60, 80] 
# #lisSub(A)
# print longest_increasing_subsequence(A)
print lisSub(A)
