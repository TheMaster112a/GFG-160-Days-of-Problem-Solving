class Solution:
    def maximumProfit(self, prices):
        # code here
        m1 = prices[0]
        res = 0
        for i in range(1, len(prices)):
            if prices[i] < m1:
                m1 = prices[i]
            
            if res < prices[i] - m1:
                res = prices[i] - m1
        return res
