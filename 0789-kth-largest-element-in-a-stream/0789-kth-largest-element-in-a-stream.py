class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # define min_heap and k
        self.min_heap = []
        self.k = k
        # add all nums in min_heap
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        # add to min_heap if we havn't processed k elements yet
        # or if val is greater than the min_heap[0]
        if len(self.min_heap) < self.k or self.min_heap[0] < val:
            heapq.heappush(self.min_heap, val)
            # pop if min_heap bigger than k
            if len(self.min_heap) > self.k:
                heapq.heappop(self.min_heap)
        return self.min_heap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)