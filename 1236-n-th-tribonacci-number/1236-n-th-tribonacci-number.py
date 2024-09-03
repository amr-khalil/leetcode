class Solution:
    def tribonacci(self, n: int) -> int:
        # dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
        # Base Cases: i0 = 0, i1 = 1, i2 = 1
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        dp = [0 for _ in range(n+1)]
        dp[1] = 1
        dp[2] = 1
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

        return dp[n]



