class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def dfs(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] != 'O':
                return
            # Mark the 'O' as temporary 'T'
            board[r][c] = 'T'
            # Explore all directions
            dfs(r-1, c)
            dfs(r+1, c)
            dfs(r, c-1)
            dfs(r, c+1)

        rows, cols = len(board), len(board[0])
        # 1. Mark the Unsurrounded regions with 'T' (O -> T)
        for r in range(rows):
            for c in range(cols):
                # It must be on the border and equal to 'O'
                if (r in [0, rows-1] or c in [0, cols-1]) and board[r][c] == 'O':
                    dfs(r, c)
        # 2. Mark the Surrounded regions with 'X' (O -> X)
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    board[r][c] = 'X'

        # 3. Revert the Unsurrounded regions to 'O' (T -> O)
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'T':
                    board[r][c] = 'O'

        