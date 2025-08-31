from typing import List


class Solution:
    def maximumProfit(self, prices) -> int:
        # code here
        tot = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                tot += prices[i] - prices[i - 1]
        return tot
