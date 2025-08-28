class Solution:
    def getSecondLargest(self, arr):
        arr = list(set(arr))
        arr = sorted(arr)
        if len(arr) == 1:
            return -1
        return arr[-2]
