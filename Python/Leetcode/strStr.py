class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle in haystack:
            for i in range(len(haystack)+1):
                if needle == haystack[i:len(needle)+i]:
                    return i
        else:
            return -1