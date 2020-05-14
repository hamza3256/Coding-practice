class Solution(object):
    def generateParenthesis(self, n):
        if n == 0:
            return []
        result = []
        self.helper(n,n,'',result)
        return result
    
    def helper(self, l, r, s, result):
        if r < l:
            return
        if l == 0 and r == 0:
            result.append(s)
        if l > 0:
            self.helper(l-1, r, s + '(', result)
        if r > 0:
            self.helper(l, r-1, s + ')', result)
            
            
        
            
            
        