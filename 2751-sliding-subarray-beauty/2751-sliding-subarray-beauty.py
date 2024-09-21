from sortedcontainers import SortedList

class Solution:
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        win_list = SortedList(nums[:k])
        num = win_list[x-1]
        ans = [num if num < 0 else 0]
        
        for r in range(k, n):
            win_list.add(nums[r])
            win_list.remove(nums[r - k])
            num = win_list[x-1]
            ans.append(num if num < 0 else 0)

        return ans