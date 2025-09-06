class Solution:
    def search(self, pat, txt):
        # code here
        c = []
        x = len(pat)
        for i in range(0, len(txt) - x + 1):
            s = txt[i:i+x]
            if s == pat:
                c.append(i)
        return c
