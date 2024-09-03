class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # one_step = cost[i-1] + dp[i-1]
        # two_steps = cost[i-2] + dp[i-2]
        # dp[i] = min(one_step, two_steps)
        # Base cases:
        # dp[0] = 0 (no cost to start)
        # dp[1] = 0 (no cost to stay on the first step)
        
        n = len(cost)
        dp = [0 for _ in range(n+1)]

        for i in range(2, len(dp)):
            one_step = cost[i-1] + dp[i-1]
            two_steps = cost[i-2] + dp[i-2]
            dp[i] = min(one_step, two_steps)

        return dp[n]