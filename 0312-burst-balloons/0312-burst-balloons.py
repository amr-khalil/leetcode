class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # coins = nums[left] * nums[i] * nums[right]
        # dp[left][right] = max(dp[left][right], coins + dp[left][i] + dp[i][right])
              
        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[0] * n for _ in range(n)]

        for length in range(2, n): # length of subarray (from 2 to n)
            for left in range(n - length): # left boundary of subarray
                right = left + length # right boundary of subarray
                # Iterate over all possible last burst balloons in the range (left, right)
                for i in range(left + 1, right):
                    coins = nums[left] * nums[i] * nums[right]
                    dp[left][right] = max(dp[left][right], coins + dp[left][i] + dp[i][right])

        print(dp)

        return dp[0][-1]