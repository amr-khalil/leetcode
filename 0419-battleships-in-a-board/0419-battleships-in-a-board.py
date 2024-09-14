class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        rows, cols = len(board), len(board[0])
        ans = 0
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'X':
                    # Check if neighbours if empty
                    if (r == 0 or board[r-1][c] != 'X') and (c == 0 or board[r][c-1] != 'X'):
                        ans += 1
        return ans