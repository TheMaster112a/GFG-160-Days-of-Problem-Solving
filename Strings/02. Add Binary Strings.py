#User function Template for python3
class Solution:
	def addBinary(self, s1, s2):
		x = int(s1, 2)
		y = int(s2, 2)
		z = x + y
		out = bin(z)[2:]
		return out
