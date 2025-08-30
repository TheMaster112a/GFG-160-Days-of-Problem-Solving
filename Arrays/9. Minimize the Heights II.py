class Solution:
    def getMinDiff(self, arr, k):
        # code here
        arr.sort()
        res = arr[-1] - arr[0] 
        x = arr[0] + k
        y = arr[-1] -k

        for i in range(len(arr) - 1):
            if arr[i + 1] - k < 0:
                continue
            
            m1 = arr[i+1] - k if arr[i + 1] - k < x else x
            m2 = arr[i] + k if arr[i] + k > y else y
            
            res = m2 - m1 if m2 - m1 < res else res
            
        return res
