class Solution:
    def findMedianSortedArrays(self, a, b):
		#finding kthe smallest when k = (a+b)//2 depending on whether its odd or even
		n = len(a)+len(b)
		if n&1:
			return self.kthSmallest(a,b,n//2+1)
		else:
			return (self.kthSmallest(a,b,n//2+1) + self.kthSmallest(a,b,n//2))/2.0
			
    def kthSmallest(self,a,b,k):
		if len(a)+len(b) < k:
			return None
		i=0
		j=0
		flag = ''
		# true for a and false for b
		while k>0:
			if i >= len(a):
				j+=1
				flag = False
			elif j >= len(b):
				i+=1
				flag = True
			elif a[i] <= b[j]:
				i+=1
				flag = True
			elif a[i] > b[j]:
				j+=1
				flag = False
			k-=1

		if flag:
			return a[i-1]
		else:
			return b[j-1]

A=Solution()
a=[]
b=[1]
print A.findMedianSortedArrays(a,b)        