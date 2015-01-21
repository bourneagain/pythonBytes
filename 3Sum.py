class Solution:
	# @return a list of lists of length 3, [[val1,val2,val3]]
	def threeSum(self, num):
		if len(num) < 3:
			return None
		res=[]
		num.sort()
		n=len(num)
		for i in range(0,n-4):
			start=i+1
			end=n-1
			while start < end:
				print i,num[i],num[start],num[end]
				if num[i]+num[start]+num[end] == 0:
					res.append((num[i],num[start],num[end]))
					start+=1
					end-=1
				elif num[i]+num[start]+num[end] > 0:
					end-=1
				else:
					start+=1
		return res
				
a=[-1,0 ,1, 2, -1, -4]
A=Solution()
print A.threeSum(a)
