class Solution:
    def numSquares(self, n: int) -> int:
        # dp[i] = min(dp[i], dp[i - j*j] + 1)
        # dp[4]= min(dp[4],dp[4−1*1]+1) = min(dp[4], dp[3]+1)
        # dp[4]= min(dp[4],dp[4−2*2]+1) = min(dp[4], dp[0]+1)
        # Base case: dp[0] = 0

        dp = [float('inf')] * (n + 1)
        dp[0] = 0

        for i in range(1, n + 1):
            j = 1
            while j**2 <= i:
                dp[i] = min(dp[i], dp[i - j**2] + 1)
                j += 1

        print(dp)
        return dp[-1]
