class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        ans = []
        scores = defaultdict(list)
        for ID, score in items:
            scores[ID].append(score)

        for ID in scores:
            top_five = heapq.nlargest(5, scores[ID])
            top_five_avg = sum(top_five) // 5
            ans.append([ID, top_five_avg])
        
        ans.sort(key=lambda x: x[0])
        return ans
