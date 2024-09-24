class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        freq = defaultdict(list)
        for ID, score in items:
            freq[ID].append(score)
        print(freq)
        ans =  [[ID, sum(sorted(scores, reverse=True)[:5]) //5] for ID, scores in freq.items()]
        ans.sort()
        return ans
