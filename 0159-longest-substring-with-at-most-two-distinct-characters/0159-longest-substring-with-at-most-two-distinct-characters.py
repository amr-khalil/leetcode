class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        l = 0
        maxLength = float('-inf')
        
        for r in range(1, len(s)+1):
            substring = s[l:r]
            while len(set(substring)) > 2 and l < r:
                l += 1
                substring = s[l:r]

            maxLength = max(maxLength, len(substring))
        
        return maxLength