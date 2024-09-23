class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        return nums[-k]
"""
pq = []
for n in nums:
    heapq.heappush(pq, n)
    if len(pq) > k:
        heapq.heappop(pq)
return pq[0]
"""