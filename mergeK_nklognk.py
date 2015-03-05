class Node:
	def __init__(self, val, array):
		self.val = val
		self.array = array
	def __lt__(self, other):
		return self.val < other.val
import random
import heapq
alist=[]
for i in list(set([random.randint(-10,50) for x in range(4)])):
	alist.append(Node(i,0))

for i in list(set([random.randint(-10,50) for x in range(4)])):
	alist.append(Node(i,1))

for i in list(set([random.randint(-10,50) for x in range(4)])):
	alist.append(Node(i,2))

print len(alist)
heapq.heapify(alist)
print len(alist)
for i in range(len(alist)):
	a=heapq.heappop(alist)
	print a.val,":",a.array


		