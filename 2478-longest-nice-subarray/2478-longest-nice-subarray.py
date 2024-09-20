class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        # &: To check if adding a new number to the window introduces any bit overlap (i.e., the window is no longer valid).
        # ^: To remove a number from the window by flipping its bits back to their previous state.
        # |: To add a new number to the window by combining its bits with the current window.
        
        n = len(nums)
        l = 0
        currWin = 0 # Start with 0 because we're accumulating the window with bitwise AND.
        max_length = 0
        for r in range(n):
            while currWin & nums[r] != 0:
                currWin ^= nums[l] # Remove the leftmost number from the window using XOR
                l += 1

            currWin |= nums[r]  # Add the current number to the window using OR
            max_length = max(max_length, r - l + 1)

        return max_length