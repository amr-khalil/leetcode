class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        # if s1[i - 1] == s2[j - 1], then dp[i][j] = diagonal (do no action)
        # else: dp[i][j] = min(up+ord(s1[i-1]), left+ord(s2[j-1]))
        # Base case:  first row = dp[i-1][0] + ord(s1[i-1]) 
        #             frist col = dp[0][j-1] + ord(s2[j-1])

        m, n = len(s1), len(s2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # Base Case
        for i in range(1, m + 1):
            dp[i][0] = dp[i-1][0] + ord(s1[i-1])
        
        # Base Case
        for j in range(1, n + 1):
            dp[0][j] = dp[0][j-1] + ord(s2[j-1])

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                up = dp[i-1][j]
                left = dp[i][j-1]
                diagonal = dp[i-1][j-1]

                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = diagonal
                else:
                    dp[i][j] = min(up + ord(s1[i-1]),
                                   left + ord(s2[j-1]))

        return dp[m][n]