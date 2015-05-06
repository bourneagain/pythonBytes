
def shortest_seek_time(A, starti):
	if not A:
		return
	mini = 99999
	begin = A[0]
	for i in A:
		if abs(i - starti) < mini:
			begin = i
			mini = abs(i - starti) 
	print begin
	A.remove(begin)
	shortest_seek_time(A, begin)




A=[11, 40, 18, 41, 9, 60, 12, 20, 31]
start = 30
shortest_seek_time(A, start)