
# priority queue with custom sorting of objects

class Test:
  def __init__(self,priority,desc):
    self.priority = priority
    self.desc = desc
    return
  def __str__(self):
    return "Priority is "+str(self.priority)
  def __gt__(self, other):
    return self.priority < other.priority
    #return self.priority < other.priority
  def __lt__(self, other):
    #return not self.priority  > other.priority
    return self.priority  < other.priority
  #def __cmp__(self,other):
  # return cmp(self.priority,other.priority)

A=Test(2,"test2")
B=Test(3,"test3")
if A>B:
  print A
# import Queue as Q
# apq=Q.PriorityQueue()
# apq.put(Test(10,'ten'))
# apq.put(Test(1,'one'))
# apq.put(Test(-1,'one'))
# apq.put(Test(12,'rwewn'))
# apq.put(Test(2,'two'))
# apq.put(Test(2,'tawo'))

# while not apq.empty():
#     next_level = apq.get()
#     print 'Processing level:', next_level.priority

# """
# class ComparableMixin:
#   def __eq__(self, other):
#     return not self<other and not other<self
#   def __ne__(self, other):
#     return self<other or other<self
#   def __gt__(self, other):
#     return other<self
#   def __ge__(self, other):
#     return not self<other
#   def __le__(self, other):
#     return not other<self
# """