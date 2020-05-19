class Solution(object):
    def reverse(self, x):
        check = math.pow(2,31)
        if x >= check-1 or x <= -check: return 0
        if x > 0:
            x = str(x)
            x = int(x[::-1])
        else:
            x = str(x)
            y = x[0]
            x = int(y + x[1:][::-1])
        if x >= check-1 or x <= -check: return 0
        else: return x
        