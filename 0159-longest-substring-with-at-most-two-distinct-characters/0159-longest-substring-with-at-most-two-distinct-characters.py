class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        # Dynamic Sliding window, one side
        
        n = len(s)
        l = 0
        maxLength = float('-inf')
        
        for r in range(n + 1):
            substring = s[l : r]
            # Filter unique character more than 2
            while len(set(substring)) > 2:
                l += 1
                substring = s[l : r]

            maxLength = max(maxLength, len(substring))
        
        return maxLength