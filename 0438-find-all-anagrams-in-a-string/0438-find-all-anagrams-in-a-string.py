class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # Rolling hash
        n = len(s)
        k = len(p)
        ans = []

        if k > n:
            return ans

        win_count = defaultdict(int)
        p_count = Counter(p)
    
        for r in range(n):
            win_count[s[r]] += 1
            if r >= k:
                if win_count[s[r - k]] == 1:
                    del win_count[s[r - k]]
                else:
                    win_count[s[r - k]] -= 1

            if p_count == win_count:
                ans.append(r - k + 1)

        return ans