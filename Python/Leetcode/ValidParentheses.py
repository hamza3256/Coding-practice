class Solution(object):
    def isValid(self, s):
        map = {'(':')', '[':']', '{':'}'}
        stack = []
        for item in s:
            if item in map:
                stack.append(item)
            else:
                if not stack:
                    return False
                if item != map[stack.pop()]:
                    return False
        if stack:
            return False
        return True