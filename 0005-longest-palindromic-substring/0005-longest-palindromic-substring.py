class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        ans = [0, 0]

        # All substrings of length 1 are palindromes
        for i in range(n):
            dp[i][i] = True
        
        # Check for substrings of length 2
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                ans = [i, i + 1]
        
        # Check for substrings longer than 2
        for diff in range(2, n ):
            for i in range(n - diff):
                j = i + diff
                # Check if s[i:j+1] is a palindrome
                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True
                    ans = [i, j]
        
        i, j = ans
        return s[i : j+1]