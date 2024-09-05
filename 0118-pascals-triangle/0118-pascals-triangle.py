class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []
        for r in range(1, numRows+1):
            triangle.append([1]*r)

        for r in range(len(triangle)):
            for c in range(len(triangle[r])):
                if c > 0 and c != r:
                    triangle[r][c] = triangle[r-1][c-1] + triangle[r-1][c]
        return triangle