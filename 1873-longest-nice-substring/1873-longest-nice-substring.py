class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        def is_nice(s):
            return len(set(s)) // 2 == len(set(s.lower()))

        n = len(s)
        ans = ''
        
        for i in range(n):
            for j in range(i + 1, n + 1):
                substring = s[i:j]
                if is_nice(substring) and len(substring) > len(ans):
                    ans = substring

        return ans