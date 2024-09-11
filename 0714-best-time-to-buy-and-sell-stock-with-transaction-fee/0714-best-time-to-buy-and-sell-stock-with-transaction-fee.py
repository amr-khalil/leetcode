class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        # Transactions = inf

        sell = 0
        buy = float('-inf')

        for price in prices:
            # Either keep the previous `sell` (do nothing) or sell the stock today.
            sell = max(sell, buy - fee + price)
            # Either keep the previous `buy` value (do nothing)or buy the stock today.
            buy =  max(buy, sell - price)

        return sell