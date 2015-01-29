class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class linkedlist:
    def addNode(self, head, data):
        newNode = Node(data)
        newNode.next = head
        return newNode
    def printlist(self, head):
        if not head:
            print "NULL LIST"
            return
        while head.next:
            print head.data,"->",
            head = head.next
        print head.data

    def count(self, head):
        if not head:
            return 0
        count = 0
        while head:
            count += 0
            head = head.next
        return count

    def getNth(self, head, n):
        if not head:
            return None
        while head:
            if n > 0:
                head = head.next
                n -= 1
            else:
                break
        assert n == 0
        return head.data

    def deleteList(self, head):
        if not head:
            return None
        while head:
            next = head.next
            del head
            head = next
        return head

    def insertNth(self, head, n, value):
        assert head != None
        while head:
            if n == 0:
                break
            else:
                n-=1
                head = head.next
        if head is None:
            assert n == 0
        newNode = Node(head.data)
        head.data = value
        newNode.next = head.next
        head.next = newNode

    def sortedinsert(self, head , n):
        ref = head
        if not head:
            return Node(n)
        elif head.data >= n:
            newNode = Node(n)
            newNode.next = head
            return newNode
        else:
            while head.next and head.next.data <= n:
                head = head.next
            newNode = Node(n)
            newNode.next = head.next 
            head.next = newNode
            return ref

    def insersort(self, head):
        res = Node(None)
        while head:
            res = self.sortedinsert(res, head.data)
            head = head.next
        return res.next

    def append(self, a, b):
        if not a:
            return b
        elif not b:
            return a

        while a.next:
            a = a.next
        a.next = b
        b = None
        return a,b

    def frontbacksplit(self, head):
        if not head:
            return None,None
        elif not head.next:
            return head,None
        a = head
        fast = head
        slow = head

        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next

        b = slow.next 
        slow.next = None
        return a,b

    def removeDups(self, head):
        if not head:
            return
        if not head.next:
            return
        while head.next:
            if head.data == head.next.data:
                head.next = head.next.next
            head = head.next

    def moveNode(self, s, d):
        newNode = s
        s = s.next
        newNode.next = d
        d = newNode
        return s,d

    def alternatingSplit(self, head):
        a = None
        b = None
        while head:
            a = self.addNode(a, head.data)
            if head.next:
                head  = head.next
                b = self.addNode(b, head.data)
            head = head.next
        return a,b

    def shuffleMerge(self, a, b ):
        res = None
        if not b:
            return a
        elif not a:
            return b

        while True:
            if a:
                a,res = self.moveNode(a,res)
                if b:
                    b,res = self.moveNode(b,res)
            else:
                break
        return res





a_list = linkedlist()
head = Node(800)
head = a_list.addNode(head, 24)
head = a_list.addNode(head, 8)
head = a_list.addNode(head, 22)
head = a_list.addNode(head, 700)
head = a_list.addNode(head, -8)

head = a_list.addNode(head, 87)
head = a_list.addNode(head, 9)
a_list.printlist(head)
a,b = a_list.alternatingSplit(head)
b = Node(None)
a_list.printlist(a)
a_list.printlist(b)

res = a_list.shuffleMerge(a,b)
a_list.printlist(res)

# head1 = Node(20)
# head1 = a_list.addNode(head1, 10)
# head1 = a_list.addNode(head1, 5)

# head2 = Node(111)
# # head2 = a_list.addNode(head2, 5)
# # head2 = a_list.addNode(head2, 22)
# # # head = a_list.addNode(head, 11)
# # # head = a_list.addNode(head, 43)
# # # head = a_list.addNode(head, 8)
# # # head = a_list.deleteList(head)
# # # a_list.printlist(head)
# # # a_list.insertNth(head,1,100)
# # # head = a_list.sortedinsert(head, 1)
# # # head = a_list.insersort(head)
# # a_list.printlist(head1)
# # a_list.printlist(head2)
# # head1,head2 = a_list.append(head1, head2)

# a_list.printlist(head1)
# a_list.printlist(head2)
# head1, head2 = a_list.moveNode(head1,head2)
# a_list.printlist(head1)
# a_list.printlist(head2)

# a,b = a_list.frontbacksplit(head)
# a_list.printlist(a)
# a_list.printlist(b)
# a_list.removeDups(head)




