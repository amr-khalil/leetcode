class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        # Base case: buy[0] = -prices[0] and sell[0] = 0
        n = len(prices)

        buy = [0] * n  # Max profit when holding a stock
        sell = [0] * n # Max profit when selling a stock

        # Base cases: on day 0, if we buy a stock, we spend prices[0], so profit is -prices[0]
        buy[0] = -prices[0]

        for i in range(1, n):
            # On day i, we either:
            # 1. Continue holding the stock from day i-1 (profit remains buy[i-1])
            # 2. Buy the stock today after selling it earlier (profit is sell[i-1] - prices[i])
            buy[i] = max(buy[i - 1], sell[i - 1] - prices[i])

            # On day i, we either:
            # 1. Continue not holding any stock from day i-1 (profit remains sell[i-1])
            # 2. Sell the stock today after buying it earlier (profit is buy[i-1] + prices[i] - fee)
            sell[i] = max(sell[i - 1], buy[i - 1] - fee + prices[i])

        # The answer is the maximum profit when selling a stock on the last day
        return sell[-1]