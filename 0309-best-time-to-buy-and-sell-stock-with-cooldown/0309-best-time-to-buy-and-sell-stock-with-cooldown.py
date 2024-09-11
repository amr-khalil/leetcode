class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Transactions = inf

        sell = 0  # Max profit after selling (or resting after selling)
        buy = float('-inf')  # Max profit after buying
        cooldown = 0  # Max profit during cooldown or resting
        
        for price in prices:
            prev_sell = sell  # Store the previous sell value
            sell = max(sell, buy + price)  # Update sell (selling today or keeping previous)
            buy = max(buy, cooldown - price)  # Update buy (buying today or keeping previous buy)
            cooldown = max(cooldown, prev_sell)  # Update cooldown (rest or after selling)
        
        # The result is the maximum profit after selling or during cooldown
        return max(sell, cooldown)