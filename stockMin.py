class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        if len(prices) == 0:
            return 0
        profit = 0
        _min = prices[0]
        for i in prices[1:]:
            _min = min(i,_min)
            profit = max(profit,i-_min)
            print _min,profit
        return profit
a=Solution()
print a.maxProfit([1,2])