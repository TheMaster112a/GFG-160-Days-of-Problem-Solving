class Solution:
    def minChar(self, s):
        rs = s[::-1]
        cs = s + '#' + rs
        n = len(cs)
        lps = [0] * n
        j = 0
        for i in range(1, n):
            while (j > 0 and cs[i] != cs[j]):
                j = lps[j-1]
            if cs[i] == cs[j]:
                j += 1
            lps[i] = j
        lpsl = lps[-1]
        return len(s) - lpsl
        
        
