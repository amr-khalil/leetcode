class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # dp[i] += dp[i - coin]
        # Base case: dp[0] = 1, There's exactly one way to make amount 0 (by using no coins).
        dp = [0] * (amount + 1)
        dp[0] = 1

        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] += dp[i - coin]
        
        return dp[-1]