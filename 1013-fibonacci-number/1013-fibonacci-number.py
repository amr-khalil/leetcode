class Solution:
    def fib(self, n: int) -> int:
        # dp[i] = dp[i-1] + dp[i-2]
        # Base Cases: i0 = 0, i1 = 1
        if n <= 1:
            return n

        dp = [0 for _ in range(n+1)]
        dp[0] = 0
        dp[1] = 1

        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        
        return dp[n]





