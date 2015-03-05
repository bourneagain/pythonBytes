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

# """
o(log(m)+log(n))
def findMedianSortedArrays(self, A, B):
    l = len(A) + len(B)
    if l % 2 == 1:
        return self.kth(A, B, l // 2)
    else:
        return (self.kth(A, B, l // 2) + self.kth(A, B, l // 2 - 1)) / 2.   

def kth(self, a, b, k):
    if not a:
        return b[k]
    if not b:
        return a[k]
    ia, ib = len(a) // 2 , len(b) // 2
    ma, mb = a[ia], b[ib]

    # when k is bigger than the sum of a and b's median indices 
    if ia + ib < k:
        # if a's median is bigger than b's, b's first half doesn't include k
        if ma > mb:
            return self.kth(a, b[ib + 1:], k - ib - 1)
        else:
            return self.kth(a[ia + 1:], b, k - ia - 1)
    # when k is smaller than the sum of a and b's indices
    else:
        # if a's median is bigger than b's, a's second half doesn't include k
        if ma > mb:
            return self.kth(a[:ia], b, k)
        else:
            return self.kth(a, b[:ib], k)
# """
