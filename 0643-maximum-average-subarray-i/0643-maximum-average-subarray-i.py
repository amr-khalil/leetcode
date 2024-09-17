class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        winSum = sum(nums[:k])
        ans = winSum

        for i in range(k, n):
            winSum += nums[i] - nums[i-k]
            ans = max(ans, winSum)

        return ans / k