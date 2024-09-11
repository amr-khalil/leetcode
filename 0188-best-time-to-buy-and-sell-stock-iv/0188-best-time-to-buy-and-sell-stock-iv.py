class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        # transactions = variable

        n = len(prices)

        # If the number of allowed transactions `k` is greater than or equal to half the number of days,
        # it's equivalent to making as many transactions as we want (unlimited transactions).
        # This is because we can't do more than n//2 transactions (one buy and one sell pair per transaction).
        if k >= n // 2:
            # In the case of unlimited transactions, we just accumulate all the positive price differences
            # This is essentially the greedy approach: buy at every local minimum and sell at the next local maximum
            return sum(max(prices[i] - prices[i - 1], 0) for i in range(1, n))

        # Initialize the `sell` array with all 0's.
        # `sell[i]` will store the maximum profit after the ith transaction, assuming we have sold the stock.
        sell = [0] * (k + 1)

        # Initialize the `buy` array with negative infinity.
        # `buy[i]` will store the maximum profit after the ith transaction, assuming we are holding a stock.
        # It's initialized to negative infinity because holding a stock at the beginning is an invalid state
        # unless we perform a "buy", so we need to set it to a very negative value.
        buy = [float("-inf")] * (k + 1)

        # Loop through each price in the `prices` array
        for price in prices:
            # For each possible transaction from 1 to k (inclusive)
            for i in range(1, k + 1):
                # Update `sell[i]` - The maximum profit after selling the stock at the ith transaction.
                # It is either the previous value (we do nothing today, hold onto the sell) or
                # we sell the stock today (which means we add the current price to the profit from `buy[i]`).
                sell[i] = max(sell[i], buy[i] + price)

                # Update `buy[i]` - The maximum profit after buying the stock at the ith transaction.
                # It is either the previous value (we do nothing today, hold onto the buy) or
                # we buy the stock today (which means we subtract the current price from the profit after the (i-1)th sell).
                buy[i] = max(buy[i], sell[i - 1] - price)

        # After processing all days, `sell[k]` will hold the maximum profit after completing at most `k` transactions
        # and not holding any stock (since we end by selling). So we return the last element of `sell`.
        return sell[k] 