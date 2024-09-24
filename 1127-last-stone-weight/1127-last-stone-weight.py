class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-stone for stone in stones]
        heapify(max_heap)

        while len(max_heap) > 1:
            first = heappop(max_heap)
            second = heappop(max_heap)

            if first != second:
                heappush(max_heap, first - second)
                
        return -max_heap[0] if max_heap else 0