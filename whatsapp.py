##################################################
# SHYAM RAJENDRAN
# srajend2@illinois.edu
# PURPOSE : creating a linked list data structure
# TO EXECUTE CODE : python whatsapp.py
####################################################
class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList:
	# to create an empty node with input data as node data and 
	# next pointer as None ( similar to NULL in C)
	def createNode(self, data):
		newNode = Node(data)
		return newNode
	
	# creates a new node and points its next pointer to head 
	# returns the node 
	def addNode(self, head, data):
		newNode = self.createNode(data)
		newNode.next = head
		return newNode

	# supporting helper function to verify the linkedlist by printing it.
	def printlist(self, head):
		if not head:	return None
		while head.next :	
			print head.data,"->",
			head = head.next
		print head.data

	# helper function to split the input list into two lists
		# it pops an element from one list and appends to other in front of its head.
	def alternateSplitList(self, head):
		ref = head
		a= None
		b= None
		while ref:
			a,ref = self.moveNode(a,ref)
			if ref:
				b,ref = self.moveNode(b,ref)
		return a,b

	# merges two input linked lists into a single sorted linked list
	def merge(self, a , b):
		toreturn = Node(None)
		if not a:
			return b
		if not b:
			return a
		if a.data <= b.data:
			toreturn = a
			toreturn.next = self.merge(a.next,b)
		else:
			toreturn = b
			toreturn.next = self.merge(a,b.next)
		return toreturn


	def mergeSort(self, head):
		if not head or not head.next :
			return head
		# The input linkedlist is split into two lists. 
		a,b = self.alternateSplitList(head)
		# recursively calling merge sort till the list is of one element 
		l = self.mergeSort(a)
		r = self.mergeSort(b)
		# use the merge function to merge the two sorted list
		merged = self.merge(l,r)
		return merged

	# pop one from source and append to head of dest ; used by the helper function alternateSplitList
	def moveNode(self,dest, source):
		newnode = source
		source = newnode.next
		newnode.next = dest
		dest = newnode
		return dest,source	

	# to check the match of two linked list
	def verifyMatch(self, a, b):
		while a:
			if a.data != b.data:
				return False
			a = a.next
			b = b.next
		return True

print " ######################################################## "
print " 	TEST 1 : CREATING AND VERIFYING THE DATASTRUCTURE "
print " ######################################################## "
print "CREATING A LINKED LIST"
list1 = LinkedList()
head = Node(90)
head = list1.addNode(head, 2)
head = list1.addNode(head, 12)
head = list1.addNode(head, 11)
head = list1.addNode(head, 43)
head = list1.addNode(head, 8)
print "PRINTING THE CREATED LIST BELOW"
list1.printlist(head)
del list1,head


print ""
print " ################################################################ "
print " 	TEST 2 : MERGING TWO SORTED LINKED LIST INTO SINGLE LIST "
print " ################################################################# "
test2 = LinkedList()
L1 = Node(15)
L1 = test2.addNode(L1, 11)
L1 = test2.addNode(L1, 9)
L1 = test2.addNode(L1, 7)
L1 = test2.addNode(L1, 5)

L2 = Node(12)
L2 = test2.addNode(L2, 8)
L2 = test2.addNode(L2, 6)
L2 = test2.addNode(L2, 4)
print "creating two linked list to test L1 and L2"
test2.printlist(L1)
test2.printlist(L2)
print "TESTING MERGE FUNCTION OF L1 and L2 to get sorted linked list "
test2.printlist(test2.merge(L1,L2))

print ""
print " ################################################################ "
print " 	TEST 3: MERGE SORT OF LINKEDLIST USING MERGE FUNCTION      "
print " ################################################################# "
test3 = LinkedList()
head = Node(90)
head = test3.addNode(head, 2)
head = test3.addNode(head, 12)
head = test3.addNode(head, 11)
head = test3.addNode(head, 43)
head = test3.addNode(head, 8)
print "PRINTING THE CREATED LIST BELOW \"BEFORE\" MERGE"
test3.printlist(head)
print "PRINTING THE CREATED LIST BELOW \"AFTER\" MERGE"
head = test3.mergeSort(head)
test3.printlist(head)


print ""
print " ################################################################ "
print " 	TEST 4 : VERIFYING THE MERGE SORT FUNCTIONALITY"
print " ################################################################ "

head2 = Node(90)
head2 = test3.addNode(head2, 43)
head2 = test3.addNode(head2, 12)
head2 = test3.addNode(head2, 11)
head2 = test3.addNode(head2, 8)
head2 = test3.addNode(head2, 2)
test3.printlist(head2)
if test3.verifyMatch(head2,head):
	print "THE MERGE SORT IS SUCCESS"
else:
	print "THE MERGE SORT FAILED"
print ""
print ""










