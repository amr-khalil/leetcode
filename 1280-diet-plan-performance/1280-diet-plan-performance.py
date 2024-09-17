class Solution:
    def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:
        n = len(calories)
        winSum = sum(calories[:k])
        if winSum < lower:
            ans = -1
        elif winSum > upper:
            ans = 1
        else:
            ans = 0

        for i in range(k, n):
            winSum += calories[i] - calories[i-k]
            if winSum < lower:
                ans -= 1
            elif winSum > upper:
                ans += 1

        return ans

