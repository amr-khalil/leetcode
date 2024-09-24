class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        # [10,3,8,9,4]
        max_heap = [(-num, idx) for idx, num in enumerate(score)]
        heapify(max_heap)

        medals = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        rank = 0
        
        while max_heap:
            _, idx = heappop(max_heap)

            if rank < len(medals):
                score[idx] = medals[rank]
            else:
                score[idx] = str(rank + 1)
            rank += 1

        return score