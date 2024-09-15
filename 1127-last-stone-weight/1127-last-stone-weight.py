class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # MaxHeap: Python dosn't have max heap, so we make all the stones negative
        stones = [-s for s in stones]
        # hepify all the stones
        heapq.heapify(stones)

        # at least two stones
        while len(stones) > 1:
            stone1 = heapq.heappop(stones)
            stone2 = heapq.heappop(stones)

            if stone1 != stone2:
                heapq.heappush(stones, stone1 - stone2)

        # Check if there is a stone left to return. Convert it back
        # to positive.
        return -heapq.heappop(stones) if stones else 0

        