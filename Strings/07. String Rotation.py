class Solution:
    def areRotations(self, s1, s2):
        s3 = s1 + s1
        
        if s2 in s3:
            return True
        return False
        
