class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # Levenshtein
        # if word1[i - 1] == word2[j - 1]: dp[i][j] = diagonal (copy the value only)
        # else: dp[i][j] = min(up, left, diagonal) + 1
        # Base Case: first row = [0..len(word1) + 1] and first col = [0..len(word2) + 1]

        m, n = len(word1), len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # Base case: if word1 is empty, we need to insert all characters of word2
        for i in range(m + 1):
            dp[i][0] = i
        
        # Base case: if word2 is empty, we need to delete all characters of word1
        for j in range(n + 1):
            dp[0][j] = j

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                up = dp[i-1][j]
                left = dp[i][j-1]
                diagonal = dp[i-1][j-1]

                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = diagonal # No operation needed
                else:
                    dp[i][j] = min(up,      # Delete
                                  left,     # Insert
                                  diagonal  # Replace
                                  ) + 1

        return dp[-1][-1]