class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        min_heap = [(sum(row), idx) for idx, row in enumerate(mat)]

        smallest = heapq.nsmallest(k, min_heap)
        ans = [idx for _, idx in smallest]
        return ans


            