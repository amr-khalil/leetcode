class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        # LPS(s) = LCS(s,reverse(s))
        # if s[i - 1] == s_reversed[j - 1], then dp[i][j] = diagonal + 1
        # else  dp[i][j] = max(up, left)
        
        s_reversed = s[::-1]
        n = len(s)

        dp = [[0] * (n + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(1, n + 1):
                up = dp[i-1][j]
                left = dp[i][j-1]
                diagonal = dp[i-1][j-1]
                
                if s[i - 1] == s_reversed[j - 1]:
                    dp[i][j] = diagonal + 1
                else:
                    dp[i][j] = max(up, left)

        return dp[-1][-1]