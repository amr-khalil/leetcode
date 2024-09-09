class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n

        for r in range(1, n):
            for l in range(r):
                if nums[l] < nums[r]:
                    dp[r] = max(dp[r], dp[l] + 1)
                    
        return max(dp)