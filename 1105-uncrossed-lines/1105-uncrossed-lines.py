class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        # nums1[i - 1] == nums2[j - 1], dp[i][j] = diagonal + 1
        # else: dp[i][j] = max(up, left)
        # Base Case: first row and col = 0
        
        m, n = len(nums1), len(nums2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                up = dp[i-1][j]
                left = dp[i][j-1]
                diagonal = dp[i-1][j-1]
                
                if nums1[i - 1] == nums2[j - 1]:
                    dp[i][j] = diagonal + 1
                else:
                    dp[i][j] = max(up, left)

        return dp[-1][-1]