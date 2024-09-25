class MedianFinder:
    """
    Two Heaps:

    A max-heap (low) to store the smaller half of the numbers.
    A min-heap (high) to store the larger half of the numbers.
    Adding a Number:

    When a new number is added, we determine which heap it should go into. If the number is less than or equal to the maximum of the low heap, it goes into low. Otherwise, it goes into high.
    After adding the number, we need to ensure that the sizes of the heaps remain balanced. The low heap can have at most one more element than the high heap.
    Finding the Median:

    If the sizes of the heaps are equal, the median is the average of the maximum of low and the minimum of high.
    If low has one more element than high, the median is the maximum of low.
    """
    def __init__(self):
        self.low = [] # Max Heap for the lower half
        self.high = [] # Min Heap for the upper half

    def addNum(self, num: int) -> None:
        # Add to max-heap (low)
        heapq.heappush(self.low, -num)  # invert the number to simulate max-heap

        # Ensure the largest number in low is <= smallest number in high
        if self.low and self.high and (-self.low[0] > self.high[0]):
            val = -heapq.heappop(self.low)
            heapq.heappush(self.high, val)

        # Balance the sizes of the heaps
        if len(self.low) > len(self.high) + 1:
            val = -heapq.heappop(self.low)
            heapq.heappush(self.high, val)
        elif len(self.high) > len(self.low):
            val = heapq.heappop(self.high)
            heapq.heappush(self.low, -val)

    def findMedian(self) -> float:
        if len(self.low) > len(self.high):
            return float(-self.low[0])
        return (-self.low[0] + self.high[0]) / 2.0



# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()