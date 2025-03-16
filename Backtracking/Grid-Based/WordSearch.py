"""
Given an m x n grid of characters board and a string word,
return True if word exists in the grid by moving adjacent (up, down, left, right) cells.

Example:
board = [["A","B","C","E"],
         ["S","F","C","S"],
         ["A","D","E","E"]]

word = "ABCCED"
Output: True
"""

def word_search(board, word):
    rows = len(board)
    cols = len(board[0])
    visited = set()
    def backtrack(r, c, index):
        if index == len(word):
            return True
        # check if out of bounds or not matching or already visited
        if (r < 0 or r >= rows 
            or c < 0 or c >= cols 
            or board[r][c] != word[index] 
            or (r, c) in visited):
            return False
        
        # mark as visited
        visited.add((r, c))
        # check if any of the 4 directions can find the next character)
        found = (backtrack(r+1, c, index+1) 
                or backtrack(r-1, c, index+1) 
                or backtrack(r, c+1, index+1) 
                or backtrack(r, c-1, index+1))
        # unmark as visited to backtrack to previous cell and try another direction
        visited.remove((r, c))
        return found
    
    # iterate through the board to find the first character of the word
    for r in range(rows):
        for c in range(cols):
            if board[r][c] == word[0]:
                if backtrack(r, c, 0):
                    return True
    return False


board = [["A","B","C","E"],
         ["S","F","C","S"],
         ["A","D","E","E"]]

word = "ABCCED"
print(word_search(board, word))
