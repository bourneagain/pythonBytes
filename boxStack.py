class Box:
	def __init__(self, length, breadth, height):
		self.length = length
		self.breadth = breadth
		self.height = height

	#custom comparition
	def __gt__(self,other):
		#return (self.length * self.breadth) > (other.length * other.breadth)
		return self.length > other.length and self.breadth > other.breadth and self.height > other.height

	
					
def solution(alist):
		max_height=-1
		ans=[-1]*(len(alist)+1)
		for i in range(0,len(alist)):
			ans[i] = alist[i].height

		for i in range(1,len(alist)):
			for j in range(0,i):
				if alist[j] > alist[i] and ans[i] < (ans[j] + alist[i].height):
					ans[i] = ans[j] + alist[i].height
		print ans
		return max(ans)


alist=[Box(1, 7, 4),Box(2, 6, 9),   Box(4, 9, 6),   Box(10, 12, 8), Box(6, 2, 5),   Box(3, 8, 5),   Box(5, 7, 7),   Box(2, 10, 16),   Box(12, 15, 9)]

print solution(alist)
