class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        l = 0
        minDiff = float('inf')

        for r in range(k-1, n):
            minDiff = min(minDiff, nums[r] - nums[l])
            l += 1

        return minDiff