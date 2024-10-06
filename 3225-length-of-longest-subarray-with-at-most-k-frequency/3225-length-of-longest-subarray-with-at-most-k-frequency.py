class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        ans = 0
        n = len(nums)
        count = defaultdict(int)
        l = 0
        for r in range(n):
            count[nums[r]] += 1
            while count[nums[r]] > k:
                count[nums[l]] -= 1
                l += 1
            ans = max(ans,  r - l + 1)
        return ans