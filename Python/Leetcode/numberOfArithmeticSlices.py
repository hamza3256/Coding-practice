class Solution(object):
    def numberOfArithmeticSlices(self, A):
        dp = [0]*len(A); sum = 0
        for i in range(2, len(A)):
            if A[i] - A[i-1] == A[i-1] - A[i-2]:
                dp[i] = 1 + dp[i-1]
                sum += dp[i]
        return sum   