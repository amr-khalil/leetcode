class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n = len(blocks)
        substring = blocks[:k]
        currBlack = substring.count('W')
        minBlack = currBlack
        for r in range(k, n):
            substring += blocks[r]
            substring = substring[1:]
            currBlack = substring.count('W')
            minBlack = min(minBlack, currBlack)

        return minBlack
