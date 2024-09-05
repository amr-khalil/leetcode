class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # dp[r][c] = 1+ min(dp[r-1][c-1], dp[r-1][c], dp[r][c-1])        
        rows, cols = len(matrix), len(matrix[0])

        dp = [[0] * cols for _ in range(rows)]
        max_side = 0
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == '1':
                    if r == 0 or c == 0:
                        dp[r][c] = 1
                    else:
                        dp[r][c] = 1 + min(dp[r-1][c-1], dp[r-1][c], dp[r][c-1])
                    max_side = max(max_side, dp[r][c])

        max_area = max_side * max_side
        return max_area