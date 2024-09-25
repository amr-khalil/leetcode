class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        projects = list(zip(capital, profits))
        n = len(projects)
        projects.sort()
        max_heap = []

        ptr = 0
        for i in range(k):
            while ptr < n and projects[ptr][0] <= w:
                heappush(max_heap, -projects[ptr][1])
                ptr += 1

            if not max_heap:
                break
            
            w += -heappop(max_heap)

        return w