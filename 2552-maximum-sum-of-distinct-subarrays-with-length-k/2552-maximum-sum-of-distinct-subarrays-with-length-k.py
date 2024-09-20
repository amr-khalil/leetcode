class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        l = 0
        win_sum = 0
        max_sum = 0
        freq = defaultdict(int)
        
        for r in range(n):
            # Add the current element to the sum
            win_sum += nums[r]
            # Increase the frequency count of the current element in the frequency map
            freq[nums[r]] += 1

            # If the window size exceeds k, shrink it from the left
            if r - l + 1 > k:
                # Decrease the frequency count of the element at the left pointer
                freq[nums[l]] -= 1
                # Remove the element's contribution to the sum
                win_sum -= nums[l]
                # If the frequency of the left element becomes zero, remove it from the hashmap
                if freq[nums[l]] == 0:
                    del freq[nums[l]]
                # Move the left pointer to the right to shrink the window
                l += 1

            # If the current window has exactly k elements and all are distinct
            if r - l + 1 == k and len(freq) == k:
                max_sum = max(max_sum, win_sum)

        return max_sum