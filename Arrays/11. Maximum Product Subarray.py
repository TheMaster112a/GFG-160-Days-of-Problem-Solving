class Solution:
	def maxProduct(self,arr):
		# code here
		max1 = float('-inf')
		maxleft, maxright = 1, 1
		
		for i in range(0, len(arr)):
		    if maxleft == 0:
		        maxleft = 1
            if maxright == 0:
		        maxright = 1
            
            maxleft *= arr[i]
            maxright *= arr[len(arr) - 1 - i]
            
            max1 = max(maxleft, maxright, max1)
            
        return max1
