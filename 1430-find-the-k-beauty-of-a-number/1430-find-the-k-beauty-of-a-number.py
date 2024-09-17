class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        numStr = str(num)
        n = len(numStr)
        win = numStr[:k]
        
        if num % int(win) == 0:
            ans = 1
        else:
            ans = 0

        for i in range(k, n):
            win += numStr[i]
            win = win[1:]

            if int(win) == 0:
                continue
            elif num % int(win) == 0:
                ans += 1
    
        return ans