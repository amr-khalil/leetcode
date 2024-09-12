class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        dp = [0, 0, 0]

        for i in range(n):
            dp0 = costs[i][0] + min(dp[1], dp[2]) # Paint house i with color 0
            dp1 = costs[i][1] + min(dp[0], dp[2]) # Paint house i with color 1
            dp2 = costs[i][2] + min(dp[0], dp[1]) # Paint house i with color 2
            dp = [dp0, dp1, dp2]
        
        return min(dp)