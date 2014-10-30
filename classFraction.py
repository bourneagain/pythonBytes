class fraction(object):
	def __init__(self,n,d):
		self.n,self.d=n,d

	def __repr__(self):
		return "X/Y=" + str(self.n) +"/" +str(self.d)


number=fraction(2,3)
print number
