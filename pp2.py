import Queue as queue
import time

prio_queue = queue.PriorityQueue()
prio_queue.put((2, time.time(), 'super blah'))
time.sleep(0.1)
prio_queue.put((1, time.time(), 'This thing would come after Some Thing if we sorted by this text entry'))
time.sleep(0.1)
prio_queue.put((1, time.time(), 'Some thing'))
time.sleep(0.1)
prio_queue.put((5, time.time(), 'blah'))

while not prio_queue.empty():
    item = prio_queue.get()
    print(item)


"""
(1, 1412382774.606068, 'This thing would come after Some Thing if we sorted by this text entry')
(1, 1412382774.70722, 'Some thing')
(2, 1412382774.504914, 'super blah')
(5, 1412382774.808372, 'blah')
"""
