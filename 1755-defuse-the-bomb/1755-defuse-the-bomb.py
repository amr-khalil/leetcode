class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        ans = [0] * n
        if k == 0:
            return ans
        
        if k > 0:
            winSum = sum(code[1:k+1])
            for i in range(n):
                ans[i] = winSum
                idx1 = (i + k + 1) % n
                idx2 = (i + 1) % n
                winSum += code[idx1] - code[idx2]

        if k < 0:
            k = -k
            winSum = sum(code[n - k: n])
            for i in range(n):
                ans[i] = winSum
                idx1 = i
                idx2 = (i - k) % n
                winSum += code[idx1] - code[idx2]

        return ans

        