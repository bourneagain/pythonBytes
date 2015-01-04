def median_of_two_sorted_arrays(a,b):
	if len(a) > len(b):
		return _median(b,a)
	else:
		return _median(a,b)
def _mo2(a,b):
	return (a+b)/2

def _mo3(*a):
	_min=min(a)
	_max=max(a)
 	return (sum(a)-(_min+_max))/2.0


def _mo4(a):
	_min=min(a)
	_max=max(a)
	median=(sum(a)-(_min+_max))/2.0
	print "MEDIAN",median
	return median


def _median(a,b):
	print "FUNC",a,b,":",
	"""
	The smaller array has only one element
	Case 1: N = 1, M = 1.
	Case 2: N = 1, M is odd
	Case 3: N = 1, M is even
	The smaller array has only two elements
	Case 4: N = 2, M = 2
	Case 5: N = 2, M is odd
	Case 6: N = 2, M is even
	"""
	n=len(a)
	m=len(b)
	b_median_index=m//2
	if n == 1:
		if m == 1:
			return _mo2(a[0],b[0])
		if m & 1:
			if 	(( a[0] < b[b_median_index] and a[0] > b[b_median_index-1] ) or 
				( a[0] > b[b_median_index] and a[0] < b[b_median_index+1] )):
				return _mo2(a[0],b[b_median_index])
			elif a[0] < b[b_median_index-1]:
				return b[b_median_index-1]
			elif a[0] > b[b_median_index+1]:
				return b[b_median_index+1]
		else:
			if a[0] > b[b_median_index-1] and a[0] < b[b_median_index]:
				return a[0]
			elif a[0] < b[b_median_index-1]:
				return b[b_median_index-1]
			elif a[0] > b[b_median_index]:
				return b[b_median_index]
	if n == 2:
		if m == 2:
			print "here"
			return _mo4(a+b)
		if m & 1:
			return _mo3(b[b_median_index], max(a[0],b[b_median_index-1]), min(a[1],b[b_median_index+1]))
		return _mo4(b[b_median_index],b[b_median_index-1],max(a[0], b[b_median_index-2]),min(a[1],b[b_median_index+1]))

	nn=(n-1)//2
	mm=(m-1)//2
	print a[nn:],b[:(mm+1)],"------",a[nn],b[mm]
	if a[nn] < b[mm]:
		return _median(a[nn:],b[:mm+1])
	return _median(a[:nn+1],b[mm:])



a=[900]
b=[5,8,10,20]
a2=[1, 12, 15, 26, 38]
b2=[2, 13, 17, 30, 45]
a3=[9]
b3=[5,8,10,20]
print median_of_two_sorted_arrays(a,b)
print "------------"
print median_of_two_sorted_arrays(a2,b2)
print "------------"
print median_of_two_sorted_arrays(a3,b3)







				

 

				




