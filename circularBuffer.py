class cicularBuffer():
	def __init__(self,size):
		self.maxsize = size
		self.buffer = [-1]*self.maxsize
		self.front = 0
		self.rear = 0
		self.bufLen = 0
	def getSize(self):
		return self.bufLen
	def isfull(self):
		return self.bufLen == self.maxsize
	def isempty(self):
		return self.bufLen == 0
	def insert(self, data):
		if not self.isfull():
			self.bufLen+=1
			self.rear  = ( self.rear + 1 ) % self.maxsize
			self.buffer[self.rear] = data
		else:
			print "buffer full"
	def pop(self):
		if not self.isempty():
			self.bufLen-=1
			self.front = (self.front + 1 )% self.maxsize
			return self.buffer[self.front]
		else:
			print "BUFFER EMPTY CANNOT POP"


abuffer = cicularBuffer(4)
abuffer.insert(2)
abuffer.insert(3)
abuffer.insert(4)
abuffer.insert(44)
print abuffer.getSize()
print abuffer.pop()
abuffer.insert(445)
print abuffer.pop()
print abuffer.pop()
print abuffer.pop()
print abuffer.pop()
print abuffer.pop()
print abuffer.pop()

# print abuffer.delete()
# print abuffer.delete()
# print abuffer.delete()
# print abuffer.delete()




