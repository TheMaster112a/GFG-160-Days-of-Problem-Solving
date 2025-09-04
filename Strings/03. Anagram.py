class Solution:
    def areAnagrams(self, s1, s2):
        
        if len(s1) != len(s2):
            return False
        s1 = sorted(s1)
        s2 = sorted(s2)
        return s1 == s2
       
