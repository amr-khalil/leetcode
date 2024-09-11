class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        # transactions = variable

        n = len(prices)
        if k >= n // 2:
            return sum(max(prices[i] - prices[i - 1], 0) for i in range(1, n))

        sell = [0] * (k + 1)
        buy = [float("-inf")] * (k + 1)

        for price in prices:
            for i in range(1, k + 1):
                sell[i] = max(sell[i], buy[i] + price)
                buy[i] = max(buy[i], sell[i - 1] - price)

        return sell[-1] 