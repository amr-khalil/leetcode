class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Heap solution O(n⋅log k) is generally more efficient than sorting O(n⋅log n),
        # particularly when k is small compared to n.
        # If k is large or k is close to n, the efficiency difference is less significant,
        # but the heap approach will still save memory O(k).
        min_heap = []
        for num in nums:
            heapq.heappush(min_heap, num)
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        return min_heap[0]