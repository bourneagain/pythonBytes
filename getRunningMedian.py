import heapq
class sol():
	def __init__(self):
		self.minh=[]
		self.maxh=[]
		return 

	def add_random(self, n):
		print n,self.minh,self.maxh," =========> ",
		if len(self.maxh) == len(self.minh):
			if len(self.minh) > 0 and self.minh[-1] != '':
				if n > self.minh[-1]:
					#self.maxh.append(n)
					heapq.heappush(self.maxh,n)
				else:
					#self.maxh.append(self.minh[-1])
					heapq.heappush(self.maxh,self.minh[-1])
					#del self.minh[-1]
					#self.minh.append(n)
					heapq.heappush(self.minh,n)
					
			else:
				#self.maxh.append(n)
				heapq.heappush(self.maxh,n)
		else:
			if n >= self.maxh[-1]:
				#self.minh.append(self.maxh[0])
				heapq.heappush(self.minh,self.maxh[0])
				del self.maxh[0]
				#self.maxh.append(n)
				heapq.heappush(self.maxh,n)
				
			else:
				#self.minh.append(n)
				heapq.heappush(self.minh,n)

		# heapq.heapify(self.minh)
		# heapq.heapify(self.maxh)
		print self.minh,self.maxh
		return
	
	def get_median(self):
		
		if len(self.maxh) == len(self.minh):
			return (self.maxh[-1]+self.minh[-1])/2.0
		else:
			return self.maxh[0]


aq=sol()
aq.add_random(0)
aq.add_random(1)
aq.add_random(5)
aq.add_random(2)
aq.add_random(3)

aq.add_random(0)
print aq.get_median()



