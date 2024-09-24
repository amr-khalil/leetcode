class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        min_heap = [(num, idx) for idx, num in enumerate(nums)]
        heapify(min_heap)
        ans = [0] * k

        while len(min_heap) > k:
            heappop(min_heap)

        # Sort the remaining elements in the heap by their original index
        min_heap.sort(key=lambda x: x[1])
        
        ans = [nums[idx] for _, idx in min_heap]
            
        return ans