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
		if not head:
			return None
		while head.next :
			print head.data,"->",
			head = head.next
		print head.data

	def deleteList(self, head, data):
		start = head
		if head.data == data:
			return head.next
		while head.next :
			if head.next.data == data:
				head.next = head.next.next
				break
			else:
				head = head.next
		return start

	def removeList(self, head):
		while head:
			prev = head
			head = head.next
			del prev
		head = None
		return head

	def findMth(self, head, m):
		ref = head
		while m+1>0:
			try:
				head = head.next
			except AttributeError:
				return -1
			m-=1

		while head:
			head = head.next
			ref = ref.next

		return ref.data
	def reverseList(self, head):
		if not head:
			return
		prev = None
		cur = head
		while cur:
			next = cur.next	
			cur.next = prev
			prev = cur	
			cur = next
		return prev

	def reverseListRecursion(self, head):
		ref = head
		if not head:
			return
		first = head
		rest = first.next
		if not rest:
			return
		self.reverseListRecursion(rest)
		first.next.next = first
		first.next = None
		head = rest





def moveNode(dest, source):
	# pop one from source and append to head of dest
	newnode = source
	source = newnode.next
	newnode.next = dest
	dest = newnode
	return dest,source



a_list = LinkedList()
head = Node(1)
head = a_list.addNode(head, 2)
head = a_list.addNode(head, 23)
head = a_list.addNode(head, 90)
head = a_list.addNode(head, 1)
head = a_list.addNode(head, 12)
# a_list.printlist(head)
# head = a_list.reverseList(head)
# a_list.printlist(head)

a_list2 = LinkedList()
head2 = Node(4)
head2 = a_list.addNode(head2, 5)
head2 = a_list.addNode(head2, 6)

print "head"
a_list.printlist(head)
print "head2"
a_list2.printlist(head2)

print "----------------DONE----------"
head,head2=moveNode(head2,head)
print "head"
a_list.printlist(head)
print "head2"
a_list2.printlist(head2)



#print a_list.findMth(head, 1)
# a_list.printlist(head)
# head = a_list.deleteList(head, 2)
# a_list.printlist(head)

# head = a_list.removeList(head)


