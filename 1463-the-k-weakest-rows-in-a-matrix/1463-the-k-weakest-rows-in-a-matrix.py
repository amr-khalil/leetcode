class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        min_heap = [(sum(row), idx) for idx, row in enumerate(mat)]
        heapify(min_heap)

        ans = [heappop(min_heap)[1] for _ in range(k)]
        return ans


            