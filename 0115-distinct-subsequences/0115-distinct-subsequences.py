class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # if s[i - 1] == t[j - 1], then dp[i][j] = diagonal + up
        # else: dp[i][j] = up
        # Base case: dp[i][0] = 1: This means any string s can generate an empty string t in exactly one way — by deleting all characters.
        
        m, n = len(s), len(t)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # Base case: Any string can match an empty string t
        for i in range(m + 1):
            dp[i][0] = 1

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                up = dp[i-1][j]
                diagonal = dp[i-1][j-1]

                if s[i - 1] == t[j - 1]:
                    # Include both possibilities: either take or leave the current character of s
                    dp[i][j] = diagonal + up
                else:
                    # Only option is to ignore the current character of s
                    dp[i][j] = up   
                    
        return dp[m][n]

"""
  0 r a b b b i t
0 0 0 0 0 0 0 0 0
r 0 1 1 1 1 1 1 1
a 0 1
b 0
b 0
i 0
t 0
"""