class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # Intuition: Look for duplicate element in the previous k elements.
        cache = {}

        for i, num in enumerate(nums):
            if num in cache:
                if abs(i - cache[num]) <= k:
                    return True
            cache[num] = i
        
        return False