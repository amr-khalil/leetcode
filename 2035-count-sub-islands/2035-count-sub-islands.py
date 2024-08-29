class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        def dfs(r, c):
            # Base case: if out of bounds or at a water cell in grid2, return True
            # True here indicates that this boundary condition does not prevent it from being a sub-island
            if r < 0 or c < 0 or r >= rows or c >= cols or grid2[r][c] == 0:
                return True

            # Mark the current cell in grid2 as visited to avoid revisiting it
            grid2[r][c] = 0

            # Assume the current component is a sub-island
            is_sub_island = True
            
            # If the corresponding cell in grid1 is water, it's not a sub-island
            if grid1[r][c] == 0:
                is_sub_island = False

            # Recursively check all four directions
            up = dfs(r-1, c)
            down = dfs(r+1, c)
            left = dfs(r, c-1)
            right = dfs(r, c+1)

            # The current cell is part of a sub-island only if all parts are sub-islands
            is_sub_island = is_sub_island and up and down and left and right

            return is_sub_island

        ans = 0
        rows, cols = len(grid2), len(grid2[0])
        for r in range(rows):
            for c in range(cols):
                if grid2[r][c] == 1:
                    if dfs(r, c):
                        ans += 1

        return ans