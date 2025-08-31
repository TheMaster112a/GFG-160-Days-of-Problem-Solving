class Solution:
    def maxSubarraySum(self, arr):
        # Code here
        res = arr[0]
        tot = arr[0]
        for i in arr[1:]:
            res = max(res+i, i)
            tot = max(res, tot)
        return tot
        
            
