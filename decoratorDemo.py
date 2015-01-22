
def a():
	return "my name is" 

def b(print_func):
		def innerfunc():
			a=print_func()
			return a.upper()
		return innerfunc

			
