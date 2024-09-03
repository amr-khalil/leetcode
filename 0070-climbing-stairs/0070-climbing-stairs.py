class Solution:
    def climbStairs(self, n: int) -> int:
        # dp[i] = dp[i-1] + dp[i-2]
        # i1 = 1, i2 = 2
        if n == 1:
            return 1
        dp = [0 for _ in range(n+1)]
        dp[1] = 1
        dp[2] = 2

        for i in range(3, len(dp)):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]