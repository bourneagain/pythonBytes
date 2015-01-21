class Solution:
	def singleNumber(self, A):
		result = 0
		# count number of -ves ; if they equal count%3 == 0 : then -ves are cancelled out
		sign = True if (sum(_<0 for _ in A))%3 else False
		val = 0 
		for i in range(32):
			# move the number i times and and with one to check if that bit is set
			# if so incr s 
			s=sum((abs(num) >> i )& 1  for num in A) % 3
			val |= s<<i
		return -1*val if sign else val
		
a=Solution()
n=[-1,-1,-1,-2,3,3,3]
#n=[16,6,6,16,6,2,16]
print a.singleNumber(n)