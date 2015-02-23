class Myhash():
	def __init__(self):
		# linked list based hash. O(n) for worst case
		self.SIZE = 10
		self.table = [[] for x in range(10)]

	def hashf(self, n):
		return n%10

	def put_(self,n, value):
		ha = self.hashf(n)
		ll = (n,value)
		self.table[ha].append((n,value))

	def get_(self, n):
		ha = self.hashf(n)
		for k,v in self.table[ha]:
			if k!=n:
				continue
			else:
				return v

a = Myhash()
a.put_(22,"sam")
a.put_(12,"sowbi")
print a.get_(12)
