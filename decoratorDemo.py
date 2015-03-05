
def a(name):
	return "my name is" + name 

# def b(print_func):
# 		def innerfunc():
# 			a=print_func()
# 			return a.upper()
# 		return innerfunc

def b(some_fuc):
	def innerfunc(*args, **kwargs):
		print args,kwargs
	return innerfunc
a(sam)

