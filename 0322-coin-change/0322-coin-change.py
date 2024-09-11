class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        fewest number of coins 
        dp[i] = min(dp[i], dp[i - coin] + 1)
        Base case: dp[0] = 0, To make amount 0, we need 0 coins.

        Example:
        coins = [5]. amount = 10 then:
        dp[10] = dp[5] + 1
        dp[5] = dp[0] + 1
        dp[0] = 0
        """

        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], dp[i - coin] + 1)

        return dp[-1] if dp[-1] != float('inf') else -1