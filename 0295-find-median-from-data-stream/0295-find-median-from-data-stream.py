class MedianFinder:

    def __init__(self):
        self.max_heap = [] # left side (negative values)
        self.min_heap = [] # right side

    def addNum(self, num: int) -> None:
        # push at the left side (max heap)
        heappush(self.max_heap, -num)
        # if the top of the left side is greater than the top of the right side
        # Then pop the value form left and push to the right
        if self.max_heap and self.min_heap and (-self.max_heap[0] > self.min_heap[0]):
            val = -heappop(self.max_heap)
            heappush(self.min_heap, val)
        # if len left > len right + 1, pop left push right
        if len(self.max_heap) > len(self.min_heap) + 1:
            val = -heappop(self.max_heap)
            heappush(self.min_heap, val)
        # elif len right > len left, pop right push left
        elif len(self.min_heap) > len(self.max_heap):
            val = heappop(self.min_heap)
            heappush(self.max_heap, -val) 

    def findMedian(self) -> float:
        # if even, take the average of top of left and right heap
        if len(self.max_heap) == len(self.min_heap):
            return (-self.max_heap[0] + self.min_heap[0]) / 2
        # if odd, return the top element in left heap
        return -self.max_heap[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()