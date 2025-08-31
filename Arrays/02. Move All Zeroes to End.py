class Solution:
	def pushZerosToEnd(self, arr):
    	c = 0
        for i in range(len(arr)):
            if arr[i] != 0:
                arr[c] = arr[i]
                c += 1
        while c < len(arr):
            arr[c] = 0
            c += 1
