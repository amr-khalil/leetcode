class Solution:
    def longestPalindrome(self, s: str) -> str:
        # dp[i][j] = (s[i] == s[j]) & (dp[i+1][j-1]) = True
        # Base Case: one character is always palindrom, dp[i][i] =  True
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        ans = [0, 0]

        # Base case: one char
        for i in range(n):
            dp[i][i] = True

        # Two chars
        for i in range(n-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                ans = [i, i+1]

        # More than two chars
        for length in range(2, n):
            for i in range(n - length):
                j = i + length
                if (s[i] == s[j]) and (dp[i+1][j-1]):
                    dp[i][j] = True
                    ans = [i, j]
        
        start, end = ans
        return s[start : end+1]