class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n = len(s)
        k = len(p)
        win_str = s[:k]
        p = sorted(p)
        ans = [0] if sorted(win_str) == p else [] 

        for r in range(k, n):
            win_str += s[r]
            win_str = win_str[1:]

            if sorted(win_str) == p:
                ans.append(r - k + 1)

        return ans

        