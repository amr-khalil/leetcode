class Solution:
    def find_median(self, max_heap, min_heap, heap_size):
        # If the window size is odd, return the root of the max_heap (negated since it's a max heap)
        if heap_size % 2 == 1:
            return -max_heap[0]
        else:
            # If even, return the average of the roots of both heaps
            return (-max_heap[0] + min_heap[0]) / 2

    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        max_heap = []  # Max heap (simulated by storing negative values)
        min_heap = []  # Min heap
        heap_dict = defaultdict(int)  # Dictionary to track elements to remove (lazy deletion)
        result = []  # List to store the results (medians)

        # Initialize heaps with the first 'k' elements
        for i in range(k):
            # Push element into max_heap, then balance by pushing the top into min_heap
            heappush(max_heap, -nums[i])
            heappush(min_heap, -heappop(max_heap))
            # If min_heap has more elements, balance by moving an element back to max_heap
            if len(min_heap) > len(max_heap):
                heappush(max_heap, -heappop(min_heap))
        
        # Get the median of the first window
        median = self.find_median(max_heap, min_heap, k)
        result.append(median)

        # Process the sliding window
        for i in range(k, len(nums)):
            prev_num = nums[i - k]  # Outgoing element (slide window)
            heap_dict[prev_num] += 1  # Mark outgoing element for lazy deletion

            # Track balance to rebalance heaps as needed
            balance = -1 if prev_num <= median else 1
            
            # Insert the new element into the appropriate heap
            if nums[i] <= median:
                balance += 1
                heappush(max_heap, -nums[i])  # Insert into max_heap if <= median
            else:
                balance -= 1
                heappush(min_heap, nums[i])  # Insert into min_heap if > median
            
            # Rebalance heaps if necessary
            if balance < 0:
                heappush(max_heap, -heappop(min_heap))  # Move element from min_heap to max_heap
            elif balance > 0:
                heappush(min_heap, -heappop(max_heap))  # Move element from max_heap to min_heap

            # Lazy deletion: Remove invalid elements from max_heap
            while max_heap and heap_dict[-max_heap[0]] > 0:
                heap_dict[-max_heap[0]] -= 1
                heappop(max_heap)
            
            # Lazy deletion: Remove invalid elements from min_heap
            while min_heap and heap_dict[min_heap[0]] > 0:
                heap_dict[min_heap[0]] -= 1
                heappop(min_heap)

            # Calculate the new median after rebalancing
            median = self.find_median(max_heap, min_heap, k)
            result.append(median)

        return result
