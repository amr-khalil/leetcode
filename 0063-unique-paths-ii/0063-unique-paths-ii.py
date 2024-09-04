class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # dp[r][c] = dp[r-1][c] + dp[r][c-1]
        # Base cases: first rows and first columns = 1, except the obstacle
        rows, cols = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * cols for _ in range(rows)]
    
        # Initialize the first cell
        dp[0][0] = 1 if obstacleGrid[0][0] == 0 else 0
        
        # Fill the first column
        for r in range(1, rows):
            if obstacleGrid[r][0] == 0:
                dp[r][0] = dp[r-1][0]  # Only can come from the cell directly above
            else:
                dp[r][0] = 0  # Block the path entirely due to obstacle
        
        # Fill the first row
        for c in range(1, cols):
            if obstacleGrid[0][c] == 0:
                dp[0][c] = dp[0][c-1]  # Only can come from the cell directly to the left
            else:
                dp[0][c] = 0  # Block the path entirely due to obstacle

        # Fill the rest of the dp table
        for r in range(1, rows):
            for c in range(1, cols):
                if obstacleGrid[r][c] == 0:
                    dp[r][c] = dp[r-1][c] + dp[r][c-1]  # Sum of the top and left cells
                else:
                    dp[r][c] = 0  # Block the path entirely due to obstacle
        
        return dp[-1][-1]