class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # 'idx' will keep track of the position of the last unique element.
        idx = 1

        # Start iterating from the second element since the first element is always unique.
        for i in range(1, len(nums)):
            # If the current element (nums[j]) is not equal to the last unique element (nums[i]),
            # it means we have found a new unique element.
            if nums[i] != nums[i-1]:
                # Update the element at the new position to the current unique element.
                nums[idx] =  nums[i]
                # Move the pointer 'i' to the next position.
                idx += 1
        
        return idx