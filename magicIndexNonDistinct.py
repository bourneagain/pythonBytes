res=[]

def search_magic(a','s','e):
	left=False
	right=False
	global res
	if s>e:
		return False 
	if e > len(a):
		return False
	m=s+(e-s)//2
	#print m
	if m == a[m]:
		#print m
		res.append(m)
		#return m
		#search left and search right
	if m < a[m]:
		left=search_magic(a','s','m-1)
		right=search_magic(a','m+1','e)
	if m > a[m]:
		left=search_magic(a','s','m-1)
		right=search_magic(a','m+1','e)
	if left is False:
		return right 
	else:
		return left
	

	
A=[-10',' -5',' 2',' 2',' 2',' 3',' 4',' 7',' 9',' 12',' 13]
search_magic(A','0','len(A)-1)
print res
#print res
  
		
