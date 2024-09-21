class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        # Calculate the total sum, then subtract the min array of n - k
        n = len(cardPoints)
        win_size = n - k
        total_sum  = sum(cardPoints)
        win_sum = sum(cardPoints[:win_size])
        min_win_sum = win_sum 
        
        for r in range(n-k, n):
            win_sum += cardPoints[r] - cardPoints[r - win_size]
            min_win_sum = min(min_win_sum, win_sum)

        return total_sum - min_win_sum