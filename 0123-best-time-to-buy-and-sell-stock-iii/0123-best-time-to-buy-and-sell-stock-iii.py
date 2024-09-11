class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # transactions = 2

        sell1 = sell2 = 0
        buy1 = buy2 = float("-inf")

        for price in prices:
            # Sell second stock or keep profit
            sell2 = max(sell2, buy2 + price)
            # Buy second stock or keep first profit
            buy2 = max(buy2, sell1 - price)

            # Sell first stock or keep profit
            sell1 = max(sell1, buy1 + price)
            # Buy first stock or keep waiting
            buy1 = max(buy1, -price)
        
        return sell2