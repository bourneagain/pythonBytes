
def lis(A):
	lis_dp = [[str(x)] for x in A]
	lis_l = [1]*len(A)
	for i in range(1,len(A)):
		for j in range(i):
			if A[j] < A[i]   and lis_l[j] + 1 > lis_l[i]:
				lis_l[i] = lis_l[j] + 1
				temp = lis_dp[j] + [str(A[i])]
				lis_dp[i]=temp
	print lis_l
	return max(lis_l),max(lis_dp,key = len)

A=[10,90,11,12,13,14,1,2,3,4]
print lis(A)
# def lisSub(A):
# 	l=[]
# 	l.append(A[0])
# 	lis=[1]*len(A)
# 	path=[str(x)+' ' for x in A]
# 	# print path

# 	for i in range(1,len(A)):
# 		#print "----"
# 		for j in range(0,i):
# 			if A[i] > A[j] and lis[j] + 1 > lis[i]:
# 				#print "BEFORE","i->",i,",j->",j,"|",A[i],A[j],"|",lis[i],lis[j]
# 				lis[i] = lis[j] + 1
# 				#print "AFTER ","i->",i,",j->",j,"|",A[i],A[j],"|",lis[i],lis[j]
# 				path[i] = path[j] + str(A[i]) + ' '
# 				print A[i],A[j],"|",path[i],"|"
# 		print ""
# 	print "PATH" ,path
# 	return max(lis),max(path,key = len)
	
# # A=[0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15] 
# A=[10, 90, 23,1,2,4,5,6] 
# A=[10,90,13,14,1,2,3,4]
# # #lisSub(A)
# # print longest_increasing_subsequence(A)
# print lisSub(A)


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


