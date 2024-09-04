class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # dp[r][c] = grid[r][c] + min(dp[r-1][c], dp[r][c-1])
        # Base case: dp[0][0] = grid[0][0]
        # dp first row = grid first row
        # dp first col = grid first col

        rows, cols = len(grid), len(grid[0])

        dp = [[0] * cols for _ in range(rows)]
        dp[0][0] = grid[0][0]
        
        for r in range(1, rows):
            dp[r][0] = grid[r][0] + dp[r-1][0]
        for c in range(1, cols):
            dp[0][c] = grid[0][c] + dp[0][c-1]

        for r in range(1, rows):
            for c in range(1, cols):
                dp[r][c] = grid[r][c] + min(dp[r-1][c], dp[r][c-1])

        return dp[-1][-1]