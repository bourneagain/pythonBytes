# MRO : method resolution order
class A:
    def p(self):
            print("inside A")

class B:
    pass

class B(A):
 pass

class C(A): 
     def p(self):
             print("inside C")

class D(B,C):
	pass

#uncomment for python 3 and check the output
#print(D.mro())
ob = D()
ob.p()
