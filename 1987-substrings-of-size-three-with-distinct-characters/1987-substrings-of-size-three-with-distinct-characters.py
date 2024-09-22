class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        n = len(s)
        k = 3
        count = 0
        win_count = defaultdict(int)
        for r in range(n):
            win_count[s[r]] += 1
            if r >= k:
                win_count[s[r - k]] -= 1
                if win_count[s[r - k]] == 0:
                    del win_count[s[r - k]]
            if len(win_count) == 3:
                count += 1
        return count