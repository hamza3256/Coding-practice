class Solution(object):
    def lengthOfLongestSubstring(self, s):
        if s == "": return 0
        if len(s) == 1: return 1
        longest = ""; l = 0; map = {}
        for i in range(len(s)):
            for j in range(i,len(s)):
                #print(longest)
                if s[j] not in longest:
                    longest += s[j]
                elif len(longest) > l:
                    l = len(longest)
                    longest = ""
                    break
                else:
                    longest = ""
                    break
        return l