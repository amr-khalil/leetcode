class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # remove duplicate form non-decreasing order array
        idx = 1
        for i in range(1, len(nums)): # the first element is always unique
            if nums[i] != nums[i-1]:
                nums[idx] = nums[i]
                idx += 1
        return idx