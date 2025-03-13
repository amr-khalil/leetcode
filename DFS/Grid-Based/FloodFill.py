"""
Problem: Flood Fill
You are given an image represented by an m x n grid of integers image, where image[i][j] represents the pixel value of the image. You are also given three integers sr, sc, and color. Your task is to perform a flood fill on the image starting from the pixel image[sr][sc].

To perform a flood fill:

Begin with the starting pixel and change its color to color.
Perform the same process for each pixel that is directly adjacent (pixels that share a side with the original pixel, either horizontally or vertically) and shares the same color as the starting pixel.
Keep repeating this process by checking neighboring pixels of the updated pixels and modifying their color if it matches the original color of the starting pixel.
The process stops when there are no more adjacent pixels of the original color to update.
Return the modified image after performing the flood fill.

Example:
Input: image = [[1,1,1],
                [1,1,0],
                [1,0,1]]
        sr = 1, sc = 1, newColor = 2
Output: [[2,2,2],
         [2,2,0],
         [2,0,1]]
"""

def floodFill(image, sr, sc, newColor):
    rows = len(image)
    cols = len(image[0])
    def dfs(r, c):
        if (
            r < 0 or
            r >= rows or
            c < 0 or
            c >= cols or
            image[r][c] != color
        ):
            return
        
        image[r][c] = newColor
        dfs(r+1, c)
        dfs(r-1, c)
        dfs(r, c+1)
        dfs(r, c-1)

    color = image[sr][sc]
    if color == newColor:
        return image
    dfs(sr, sc)

    return image



image = [[1,1,1],
         [1,1,0],
         [1,0,1]]
sr = 1
sc = 1
newColor = 2
print(floodFill(image, sr, sc, newColor)) # [[2,2,2],[2,2,0],[2,0,1]]