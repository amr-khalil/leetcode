class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        n = len(s)
        l = 0
        maxLength = 0

        for r in range(1, n + 1):
            substring = s[l : r]

            while len(set(substring)) > k:
                l += 1
                substring = substring[l:]
        
            maxLength = max(maxLength, len(substring))

        return maxLength