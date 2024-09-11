class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # transactions = 1
        
        sell = 0
        buy = float("-inf")

        for price in prices:
            # Either keep the previous sell or sell today
            sell = max(sell, buy + price)
            # Either keep the previous buy or buy today
            buy = max(buy, -price)

        return sell
