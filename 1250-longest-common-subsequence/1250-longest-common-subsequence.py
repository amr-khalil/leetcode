class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + 1
        # Base case: first col = 0 and first row = 0

        rows = len(text1)
        cols = len(text2)

        dp = [[0] * (cols+1) for _ in range(rows+1)]

        for i in range(1, rows+1):
            for j in range(1, cols+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        return dp[-1][-1]