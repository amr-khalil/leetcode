class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Transactions = inf
        
        sell = 0
        buy = float('-inf')
        cooldown = 0

        for price in prices:
            buy = max(buy, cooldown-price)
            cooldown = max(cooldown, sell)
            sell = max(sell, buy + price)

        return max(sell, cooldown)