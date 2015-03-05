class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        
        result = 0
        for i in A:
        	result^=i
        return result
a=Solution()
# n=[1,1,3,3,5,4,4]
n = [1,2,3,4]
print a.singleNumber(n)