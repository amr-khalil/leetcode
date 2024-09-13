class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # Get lengths of string 's' and pattern 'p'
        m, n = len(s), len(p)

        # Initialize the DP table with False. 
        # dp[i][j] will be True if the first i characters of 's' match the first j characters of 'p'.
        dp = [[False] * (n + 1) for _ in range(m + 1)]

        # Base case: Empty pattern matches empty string
        dp[0][0] = True

        # Handle cases where the pattern can match an empty string (e.g. "a*" or ".*")
        for j in range(1, n + 1):
            if p[j - 1] == '*' and j > 1:
                # '*' can eliminate the previous character, so we look back two positions
                dp[0][j] = dp[0][j - 2]
       
        # Fill the DP table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # If current characters in 's' and 'p' match or if there's a '.', it's a match
                if p[j - 1] == '.' or p[j - 1] == s[i - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                
                # If the current character in 'p' is '*', we need to consider zero or more occurrences
                elif p[j - 1] == '*' and j > 1:
                    # Case 1: '*' represents zero occurrence of the previous character
                    dp[i][j] = dp[i][j - 2]
                    
                    # Case 2: '*' represents one or more occurrences
                    if p[j - 2] == '.' or p[j - 2] == s[i - 1]:
                        dp[i][j] = dp[i][j] or dp[i - 1][j]
        
        print(dp)
        # Return whether the entire string 's' matches the pattern 'p'
        return dp[-1][-1]

"""
  0 c * a * b
0 y n y n y n
a n n n y y n
a n n n n y n
b n n n n n y
"""