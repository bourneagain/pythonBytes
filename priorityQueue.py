from Queue import PriorityQueue
import time
class MyPriorityQueue(PriorityQueue):
    def __init__(self):
        PriorityQueue.__init__(self)
        self.counter = 0

    def put(self, item, priority):
        PriorityQueue.put(self, (priority, self.counter, item))
        self.counter +=  

    def get(self, *args, **kwargs):
        _, _, item = PriorityQueue.get(self, *args, **kwargs)
        return item


queue = MyPriorityQueue()
queue.put('item2', time.time(),)
queue.put('item1', 1)

print queue.get()
print queue.get()
print queue.counter
