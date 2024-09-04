class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        # dp[i] = max(dp[i-1], dp[i-2]+costs[i])
        # Base cases: i0 = 0, i1 = costs[1]
        if not nums:
            return 0

        n = max(nums)
        costs = [0 for _ in range(n+1)]
        for num in nums:
            costs[num] += num

        dp = [0 for _ in range(n+1)]
        dp[0] = 0
        dp[1] = costs[1]
        for i in range(2, n+1):
            dp[i] = max(dp[i-1], dp[i-2]+costs[i])

        return dp[n]