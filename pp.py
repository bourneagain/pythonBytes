import Queue as queue

prio_queue = queue.PriorityQueue()
prio_queue.put((2, 8, 'super blah'))
prio_queue.put((1, 4, 'Some thing'))
prio_queue.put((1, 3, 'This thing would come after Some Thing if we sorted by this text entry'))
prio_queue.put((5, 1, 'blah'))

while not prio_queue.empty():
    item = prio_queue.get()
    print(item)
"""
(1, 3, 'This thing would come after Some Thing if we sorted by this text entry')
(1, 4, 'Some thing')
(2, 8, 'super blah')
(5, 1, 'blah')
"""
