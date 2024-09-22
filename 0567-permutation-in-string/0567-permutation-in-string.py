class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s2)
        k = len(s1)

        # Base case: If s1 is longer than s2, no permutation is possible
        if k > n:
            return False
        
        win_count = defaultdict(int)
        s1_count = Counter(s1)
        for r in range(n):
            win_count[s2[r]] += 1

            if r >= k:
                if win_count[s2[r - k]] == 1:
                    del win_count[s2[r - k]]
                else:
                    win_count[s2[r - k]] -= 1
            
            if s1_count == win_count:
                return True

        return False