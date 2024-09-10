class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # if price[i] > price[i - 1]: dp[i] = dp[i - 1] + (price[i] - price[i - 1])
        # else: dp[i] = dp[i - 1]
        # Base case: dp[0] = 0, no profit
        
        n = len(prices)
        dp = [0] * n

        for i in range(1, n):
            profit = prices[i] - prices[i - 1]
            if profit > 0:
                dp[i] = dp[i - 1] + profit
            else:
                dp[i] = dp[i - 1]
                
        return dp[-1]