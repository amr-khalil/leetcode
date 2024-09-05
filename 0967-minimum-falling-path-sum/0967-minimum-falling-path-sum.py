class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        # dp[r][c] = min(dp[r-1][c-1], dp[r-1][c]) + matrix[r][c]
        # Base Case: firs row in db = first row in matrix
        rows, cols = len(matrix), len(matrix[0])
        dp = [[0]*cols for _ in range(rows)]
        dp[0] = matrix[0]

        for r in range(1, rows):
            for c in range(cols):
                if c == 0:
                    dp[r][c] = min(dp[r-1][c], dp[r-1][c+1]) + matrix[r][c]
                elif c == rows-1:
                    dp[r][c] = min(dp[r-1][c-1], dp[r-1][c]) + matrix[r][c]
                else:
                    dp[r][c] = min(dp[r-1][c-1], dp[r-1][c], dp[r-1][c+1]) + matrix[r][c]

        return min(dp[-1])