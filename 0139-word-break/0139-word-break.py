class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)
        n = len(s)
        dp = [False for _ in range(n+1)]
        dp[0] = True

        for length in range(1, n+1):
            for start in range(length):
                if dp[start] and s[start:length] in word_set:
                    dp[length] = True
                    break
        
        return dp[-1]