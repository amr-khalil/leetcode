import bisect
class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        n = len(nums)
        ans = []
        winList = []
        for i in range(n):
            if i >= k:
                winList.remove(nums[i-k])
            bisect.insort(winList, nums[i])
        
            if i >= k - 1:
                if k % 2 == 1:
                    ans.append(winList[k//2])
                else:
                    ans.append((winList[k//2 - 1] + winList[k//2]) / 2)
        return ans