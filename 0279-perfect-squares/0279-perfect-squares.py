class Solution:
    def numSquares(self, n: int) -> int:
        # dp[i] stores the minimum number of perfect squares that sum to 'i'
        # dp[i] = min(dp[i], dp[i - j*j] + 1)
        # Example: dp[4]= min(dp[4], dp[4−1*1]+1) = min(dp[4], dp[3]+1)
        #          dp[4]= min(dp[4], dp[4−2*2]+1) = min(dp[4], dp[0]+1)
        # Base case: dp[0] = 0 (it takes 0 squares to make 0)

        dp = [float('inf')] * (n + 1)
        dp[0] = 0

        squares = [i**2 for i in range(1, int(math.sqrt(n))+ 1)]
        
        for square in squares:
            for i in range(square, n + 1):
                dp[i] = min(dp[i], dp[i- square] + 1)

        return dp[-1]

