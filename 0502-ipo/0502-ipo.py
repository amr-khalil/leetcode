class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        projects = list(zip(capital, profits))
        min_heap = [(capital, profit) for capital, profit in projects] # for capital
        heapify(min_heap)
        max_heap = [] # for profit

        # Perform up to k projects
        for i in range(k):
            while min_heap and min_heap[0][0] <= w:
                # Move all projects that are affordable (capital requirement <= current capital w) to the profit heap
                capital, profit = heappop(min_heap)
                # Push the profit into the max-heap (use negative to simulate a max-heap)
                heappush(max_heap, -profit)
            # If no project is affordable, we break
            if not max_heap:
                break
            # Pop the most profitable project and increase the capital
            w += - heappop(max_heap)
        return w