class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []
        
        for i in range(len(points)):
            x, y = points[i]
            dist = -(x**2 + y**2)
            heappush(max_heap, (dist, i))
            if len(max_heap) > k:
                heappop(max_heap)

        return [points[i] for _, i in max_heap]