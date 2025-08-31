class Solution:
    def maxCircularSum(self, arr):
        # code here
        tot, m1, m2, cm1, cm2 = 0,arr[0],arr[0],0,0
        
        for i in arr:
            cm2 = max(cm2 + i, i)
            m2 = max(m2, cm2)
            
            cm1 = min(cm1 + i, i)
            m1 = min(m1, cm1)
            
            tot += i
            
        if m1 == tot:
            return m2
        return max(m2, tot - m1)
        
