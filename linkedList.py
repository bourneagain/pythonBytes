class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList:
	def createNode(self, data):
		newNode = Node(data)
		return newNode
	def addNode(self, head, data):
		newNode = self.createNode(data)
		newNode.next = head
		return newNode

	def printlist(self, head):
		while head.next :
			print head.data,"->",
			head = head.next
		print head.data

a_list = LinkedList()
head = Node(1)
head = a_list.addNode(head, 2)
head = a_list.addNode(head, 23)
head = a_list.addNode(head, 90)

a_list.printlist(head)