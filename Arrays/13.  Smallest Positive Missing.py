class Solution:
    def missingNumber(self, arr):
        arr.sort()
        m = 1
        for i in arr:
            if i <= 0:
                continue
            else:
                if i < m:
                    continue
                elif i == m:
                    m+=1
                else:
                    return m
        return m
