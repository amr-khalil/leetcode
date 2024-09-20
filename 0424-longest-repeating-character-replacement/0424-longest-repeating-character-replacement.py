class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        l = 0
        freq = defaultdict(int)
        max_freq = 0
        max_length = 0
        for r in range(n):
            window_size = r - l + 1
            freq[s[r]] += 1
            max_freq = max(freq.values())

            if window_size - max_freq > k:
                freq[s[l]] -= 1
                l += 1
            max_length = max(max_length, r - l + 1)

        return max_length
