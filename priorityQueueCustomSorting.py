
# priority queue with custom sorting of objects

class Test:
	def __init__(self,priority,desc):
		self.priority = priority
		self.desc = desc
		return
	def __cmp__(self,other):
		return cmp(self.priority,other.priority)

import Queue as Q
apq=Q.PriorityQueue()
apq.put(Test(10,'ten'))
apq.put(Test(1,'one'))
apq.put(Test(12,'rwewn'))
apq.put(Test(2,'two'))

while not apq.empty():
    next_level = apq.get()
    print 'Processing level:', next_level.desc

"""
class ComparableMixin:
  def __eq__(self, other):
    return not self<other and not other<self
  def __ne__(self, other):
    return self<other or other<self
  def __gt__(self, other):
    return other<self
  def __ge__(self, other):
    return not self<other
  def __le__(self, other):
    return not other<self
"""