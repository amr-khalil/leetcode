class Solution:
    def minInsertions(self, s: str) -> int:
        # Minimum insertions is the difference between string length and LCS length
        # n - lcs_length
        # s[i - 1] == s_reversed[j - 1] => dp[i][j] = diagonal + 1
        # else dp[i][j] = max(up, left)
        
        n = len(s)
        s_reversed = s[::-1]
        dp = [[0] * (n + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(1, n + 1):
                up = dp[i-1][j]
                left = dp[i][j-1]
                diagonal = dp[i-1][j-1]

                if s[i - 1] == s_reversed[j - 1]: 
                    dp[i][j] = diagonal + 1 # Match: extend the LCS
                else:
                    dp[i][j] = max(up, left) # Mismatch: take the longer subsequence

        lcs_length = dp[-1][-1]
        return n - lcs_length
"""
  0 m b a d m
0 0 0 0 0 0 0
m 0 1 1 1 1 1
d 0 1 1 1 2 1
a 0 1 1 2 2 2
b 0 1 2 2 2 2
m 0 1 2 2 2 2
"""