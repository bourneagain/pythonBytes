

def search_array(array,x):
	return search(array,0,len(array)-1,x)

def search(a,start,end,x):
	print a[start:end+1]
	if start > end:
		return search_liner(a,x) 
	if x == a[start]:
		return start
	if x == a[end]:
		return end
	mid = start + (end-start)//2
	if x == a[mid]:
		return mid

	if a[start] < a[mid]:
		#left sorted
		print "here 1"
		if x >= a[start] and x <= a[mid]:
			# x is in here use bst
			return search(a,start,end-1,x)
		else:
			return search(a,mid+1,end,x)
	elif a[mid] > a[end]:
		print "here 2"
		# right sorted
		if x >= a[mid] and x <= a[end]:
			# x here 
			return search(a,mid+1,end,x)
		else:
			return search(a,start,mid-1,x)
	else:
		print "here 3"
		if a[start] == a[mid]:
			return search(a,mid+1,end,x)
		else:
			return search(a,start,mid-1,x)
		
def search_liner(a,x):
	print "failure : linear"
	for c,i in enumerate(a):
		if i==x:
			return c

a=[1, 1, 0, 1, 1, 1, 1]
a=[5,5,5,5,5,1,2]
print search_array(a,1)
