class Solution:
    def myAtoi(self, s):
        s = s.lstrip()
        
        if not s:
            return 0
            
        sign = 1
        
        if s[0] == '-':
            sign *= -1
            s = s[1:]
        
        
        result = 0
        
        for i in s:
            if i.isdigit():
                result = result * 10 + ord(i) - ord('0')
            else:
                break
        result *= sign
        
        m1, m2 = 2 ** 31 - 1, (2 ** 31) * -1
        
        if result > m1:
            return m1
        if result < m2:
            return m2
        
        return result
