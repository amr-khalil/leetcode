class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        # - buy[i]: max profit on day i if we are holding a stock
        # - sell[i]: max profit on day i after selling a stock
        # - cooldown[i]: max profit on day i if we are in cooldown (no stock)
        buy = [0] * n
        sell = [0] * n
        cooldown = [0] * n

        # Base cases: # - If we buy on day 0, profit is negative the price on day 0 (-prices[0])
        buy[0] = -prices[0]
        sell[0] = 0 # no sell
        cooldown[0] = 0 # no cooldown

        for i in range(1, n):
            # On day i, if we are holding a stock, we can either:
            # 1. Continue holding from day i-1 (buy[i-1])
            # 2. Buy today after being in cooldown yesterday (cooldown[i-1] - prices[i])
            buy[i] = max(buy[i - 1], cooldown[i - 1] - prices[i])

            # On day i, if we sell a stock, we must have been holding it on day i-1, 
            # so the profit is buy[i-1] + prices[i]
            sell[i] = buy[i - 1] + prices[i]

            # On day i, if we are in cooldown, we can either:
            # 1. Continue being in cooldown from day i-1 (cooldown[i-1])
            # 2. Enter cooldown after selling a stock yesterday (sell[i-1])
            cooldown[i] = max(cooldown[i - 1], sell[i - 1])

        # The result will be the maximum profit on the last day when we are not holding a stock.
        # This means we either sold a stock on the last day or we are in a cooldown state.
        return max(sell[-1], cooldown[-1])