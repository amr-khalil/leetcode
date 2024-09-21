class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        win_size = 2*k + 1
        win_sum = sum(nums[:win_size])
        ans = [win_sum // win_size if k > 0 else win_sum]
        if k == 0:
            return nums
        if win_size > n:
            return [-1] * n

        for r in range(win_size, n):
            win_sum += nums[r] - nums[r-win_size]
            ans.append(win_sum//win_size if k > 0 else 0)
        t = (n - len(ans)) // 2
        return [-1] * t +  ans + [-1] * t