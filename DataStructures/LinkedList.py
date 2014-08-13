"""
Implementation of Node : linked list in Python
"""
class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext



if False:
        linkedList=Node("23")
    print linkedList.getData()
     linkedList.setData("123")
        print linkedList.getData()
    linkedList.setNext("890")
    print linkedList.getNext()
"""