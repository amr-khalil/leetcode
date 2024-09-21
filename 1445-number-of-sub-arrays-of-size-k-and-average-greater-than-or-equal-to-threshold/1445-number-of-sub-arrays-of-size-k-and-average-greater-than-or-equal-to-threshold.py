class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        n = len(arr)
        win_sum = sum(arr[:k])
        cnt_sub_array = 1  if (win_sum / k) >= threshold else 0
        for r in range(k, n):
            win_sum += arr[r] - arr[r - k]
            if (win_sum / k) >= threshold:
                cnt_sub_array += 1
        
        return cnt_sub_array