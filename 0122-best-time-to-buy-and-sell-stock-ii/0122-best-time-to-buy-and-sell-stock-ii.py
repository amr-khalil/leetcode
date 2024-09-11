class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # transactions = inf

        sell = 0
        buy = float("-inf")

        for price in prices:
            # Sell the stock or keep the profit
            sell = max(sell, buy + price)
            # Buy a new stock or keep the old one
            buy =  max(buy, sell - price)

        return sell
