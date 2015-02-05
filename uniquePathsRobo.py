def magic_index(A):
	# return magic_index_helper(A,0,len(A))
	return magic_index_non_distinct(A,0,len(A))

def magic_index_helper(A, start, end):	
	if start > end:
		return None
	mi = (start + end )//2
	mv = A[mi]
	if mv == mi : 
		return mv
	elif mv < mi:
		return magic_index_helper(A,mi+1 , end)
	else:
		return magic_index_helper(A,start, mi-1)

def magic_index_non_distinct(A,start , end):
	if start > end:
		return None
	mi = (start + end )//2
	mv = A[mi]
	if mv == mi : 
		return mv
	elif mv < mi:
		start = max(mi+1,mv)
		return magic_index_helper(A,start , end)
	else:
		end = min(mi-1,mv)
		return magic_index_helper(A,start, end)		

A=[-10,-5,2,2,2,3,4,6,9,12,13]
print magic_index(A)
