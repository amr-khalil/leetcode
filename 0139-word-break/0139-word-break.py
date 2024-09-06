class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # dp[start] & s[start:length] in word_set, prefix word can be segmentet and word in dict.
        # Base case: dp[0] = True, where an empty string can always be segmented

        # Convert wordDict to a set for fast lookup (O(1) time complexity for checking existence)
        word_set = set(wordDict)
        n = len(s)
        # Initialize the DP array of size n+1, where dp[i] represents whether the substring s[0:i] can be segmented
        dp = [False for _ in range(n+1)]
        dp[0] = True

        for length in range(1, n+1):
            for start in range(length):
                # Check if the substring s[start:length] is in the dictionary (word_set) and 
                # if the prefix s[0:start] can be segmented (dp[start] is True)
                if dp[start] and s[start:length] in word_set:
                    dp[length] = True
                    break
        
        return dp[-1]