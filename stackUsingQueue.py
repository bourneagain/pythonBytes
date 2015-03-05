import Queue
class myStack():
	def __init__(self, size):
		self.q1 = Queue.Queue()
		self.q2 = Queue.Queue()
		self.size = size
		self.qsize = 0

	def isempty(self):
		return self.qsize == 0
	def isfull(self):
		return self.qsize == self.size
	def push(self, data):
		if not self.isfull():
			self.q1.put(data)
			self.qsize+=1
		else:
			print "FULL"
	def pop(self):
		if not self.isempty():
			while self.q1.qsize() > 1:
				self.q2.put(self.q1.get(False))
			t = self.q1.get(False)
			self.q1,self.q2 = self.q2,self.q1
			self.qsize-=1
			return t
		else:
			print "EMTPY"

astack = myStack(3)
astack.push(1)
astack.push(3)
astack.push(4)

print astack.pop()
print astack.pop()
astack.push(12)
print astack.pop()




