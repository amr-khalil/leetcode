class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        n = len(colors)
        k = 3
        winList = colors[:k]
        count = 1 if winList in [[1, 0, 1], [0, 1, 0]] else 0

        for r in range(k, n + k - 1):
            index = r % n
            winList.append(colors[index])
            winList = winList[1:]
            count += 1 if winList in [[1, 0, 1], [0, 1, 0]] else 0 

        return count
