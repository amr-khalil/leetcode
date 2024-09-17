class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        n = len(s)
        k = 3

        substring = s[:k]
        ans = 1 if len(set(substring)) == k else 0

        for i in range(k, n):
            substring += s[i]
            substring = substring[1:]
            
            if len(set(substring)) == k:
                ans += 1

        return ans