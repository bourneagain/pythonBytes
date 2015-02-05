import collections
class RandomListNode:	 def __init__(self, x):		 self.label = x		 self.next = None		 self.random = None

class Solution:
	def copyRandomList(self, head):
		ref = head
		check=collections.defaultdict()
		check[None] = None
		if not head:	return None
		while head:	check[head] = RandomListNode(head.label)	head = head.next	head = ref
		while head:	check[head].next = check[head.next]	head = head.next
		head = ref
		while head:	check[head].random = check[head.random]	head = head.next	return check[ref]


def printlist(head):
	while head:
		print head.label
		head = head.next

n = RandomListNode(1)n2 = RandomListNode(2)
n2 = RandomListNode()
n.next = n2	a = Solution()
b = a.copyRandomList(n)
printlist(b)
