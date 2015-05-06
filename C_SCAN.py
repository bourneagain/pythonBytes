
def C_SCAN(A, starti):
	
	mini = 99999
	rotate_value = A[0]
	for i in A:
		if abs(i - starti) < mini:
			rotate_value = i
			mini = abs(i - starti) 
	A.sort()
	pivot = A.index(rotate_value)
	print A[pivot:]+A[:pivot]

A=[11, 40, 18, 41, 9, 60, 12, 20, 31]
start = 30
C_SCAN(A, start)