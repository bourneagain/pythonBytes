"""
Sample implementation of the dequeue datastructure in python
"""
class Dequeue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addFront(self, item):
        self.items.append(item)

    def addRear(self, item):
        self.items.insert(0,item)

    def delFront(self):
        return self.items.pop()

    def delRear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)
