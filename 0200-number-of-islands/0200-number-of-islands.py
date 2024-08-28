class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(r, c):
            # Check if current cell is out of bounds or is water ('0')
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == '0':
                return
            # Mark the cell as visited by setting it to '0' (to avoid revisiting)
            grid[r][c] = '0'          
            # Recursively visit all neighboring cells
            dfs(r-1, c)
            dfs(r+1, c)
            dfs(r, c-1)
            dfs(r, c+1)

        ans = 0
        rows, cols = len(grid), len(grid[0])
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    ans += 1
                    dfs(r, c)
        
        return ans