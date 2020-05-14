class Solution(object):
    def romanToInt(self, s):
        rn = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        x = prev = 0; lenS = len(s)-1
        for i in range(lenS,-1,-1):
            if rn[s[i]] >= prev:
                x += rn[s[i]]
                prev = rn[s[i]]
            else:
                x -= rn[s[i]]
        return x