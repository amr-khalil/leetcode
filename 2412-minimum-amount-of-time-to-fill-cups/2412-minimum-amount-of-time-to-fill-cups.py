class Solution:
    def fillCups(self, amount: List[int]) -> int:
        # Create a max-heap by inserting negative values of amount
        max_heap = [-n for n in amount if n > 0]
        heapify(max_heap)
        time = 0

        # Continue until the heap is empty (all cups are filled)
        while len(max_heap) > 1:
            # Pop the two largest elements
            largest = -heappop(max_heap)
            second_largest = -heappop(max_heap)

            # Fill two cups, one from each of the largest two
            largest -= 1
            second_largest -= 1

            # Push the decremented values back if they are still greater than 0
            if largest > 0:
                heappush(max_heap, -largest)
            if second_largest > 0:
                heappush(max_heap, -second_largest)

            time += 1 # Increment time by 1 second
        
        # If there is one remaining element, fill the remaining cups one at a time
        if max_heap:
            time = time - max_heap[0]
        
        return time