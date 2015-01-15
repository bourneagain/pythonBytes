from collections import OrderedDict
class LRUCache:
	def __init__(self, capacity):
		self.capacity = capacity
		self.cache  = OrderedDict()

	def set(self, key, value):
		if key not in self.cache:
			if len(self.cache) > self.capacity:
				self.cache.popitem(last=False)
			self.cache[key]=value
		else:
			print self.cache,key
			self.cache.pop(key)
			self.cache[key]=value

	def get(self, key):
		if key not in self.cache:
			return -1
		else:
			return self.cache[key]

	def print_cache(self):
		print self.cache


sol=LRUCache(5)
sol.set(1,"sam")
sol.set(2,"s")
sol.set(3,"sm")
sol.set(4,"sasd")
sol.set(5,"ssadasdm")
sol.set(2,"saadm")
sol.set(3,"saadadm")
sol.set(7,"ssadasdm")
# sol.set(8,"ssadasdm")
# sol.set(9,"ssadasdm")
# sol.set(10,"ssadasdm")
sol.print_cache()




