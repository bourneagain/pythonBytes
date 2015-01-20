class Solution:
	def singleNumber(self, A):
		result = 0
		sflag=False
		if sum(A) < 0:
			sflag=True
			A=[-1*x for x in A]
		for i in xrange(0,64):
			x = 1<<i;s=0
			for i in A:
				if i&x:
					s+=1
			if s%3:
				result |=x
			#rint result,s
		return -1 * result if sflag else result
a=Solution()
n=[-1,-1,-1,-2,-3,-3,-3]
n=[16,6,6,16,6,2,16]
print a.singleNumber(n)