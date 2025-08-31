class Solution:
    def findMajority(self, arr):
        # code here
        d = {}
        x = []
        for i in arr:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        f = len(arr) / 3
        for i in d:
            if d[i] > f:
                x.append(i)
        x.sort()
        return x
