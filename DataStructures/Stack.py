"""
Sample implementation of the stack datastructure in python
"""
import sys
if __name__ != '__main__':
        print "this Stack module is IMPORTED AND NOT A MAIN PROGRAM"
        #sys.exit()
else:
	print "calling main method"

class Stack(object):
	def __init__(self):
		self.items=[]

	def isEmpty(self):
		return self.items == []
	
	def push(self,item):
		self.items.append(item)

	def pop(self):
		return self.items.pop()

	def peek(self):
		return self.items[len(self.items)-1]	

	def size(self):
		return len(self.items)



binaryNum=Stack()
print binaryNum.size()
