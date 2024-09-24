class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Create a list of tuples containing each element in nums and its index
        # (num, idx) represents the value and its position in the original array.
        min_heap = [(num, idx) for idx, num in enumerate(nums)]
        
        # Step 2: Convert the list of tuples into a min-heap
        # This organizes the elements in nums based on their values, with the smallest at the root.
        heapify(min_heap)
        
        # Step 3: Keep only the largest k elements in the heap
        # Repeatedly remove the smallest elements from the heap until its size is reduced to k.
        while len(min_heap) > k:
            heappop(min_heap)

        # Step 4: Sort the remaining k elements in the heap by their original index
        # This ensures that the subsequence is returned in the same order as they appeared in the original array.
        min_heap.sort(key=lambda x: x[1])
        
        # Step 5: Extract the values from the nums array based on the sorted indices
        # Build the final result by accessing the original nums array using the stored indices.
        ans = [nums[idx] for _, idx in min_heap]
        
        # Step 6: Return the resulting subsequence of k largest elements in the original order
        return ans