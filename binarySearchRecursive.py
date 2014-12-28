
def binary_search(aList, ele, start, end):
	mid=start + (end-start)//2
	#print mid
	if start > end:
		return -1
	if start == end:
		return -1
	if ele == aList[0]:
		return 0
	elif ele == aList[-1]:
		return len(aList)-1
	if ele == aList[mid]:
		return mid

	if ele < aList[mid]:
		return binary_search(aList,ele,0,mid)
	elif ele > aList[mid]:
		return binary_search(aList,ele,mid+1,end)

A=[]
print binary_search(A, 1, 0, len(A))
A=[1]
print binary_search(A, 1, 0, len(A))
A=[1]
print binary_search(A, 2, 0, len(A))
A=[1]
print binary_search(A, -1, 0, len(A))
A=[1,5]
print binary_search(A, 5, 0, len(A))

	

	