class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        A = prices
        if len(prices) == 0:
            return 0
        elif len(prices) == 1:
            return 0
        elif len(prices) == 2:
            if A[1] > A[0]:
                return A[1] - A[0]
            else:
                return 0
        minv = min(A[0],A[1])
        if A[1] > A[0]:
            maxdiff = A[1] - A[0]
        else:
            maxdiff = 0

        for i in A[2:]:
            minv = min(minv,i)
            maxdiff = max(maxdiff,i-minv)
            #print minv,maxdiff
        return maxdiff
