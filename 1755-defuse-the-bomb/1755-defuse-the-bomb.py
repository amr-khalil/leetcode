class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
    
        # If k is 0, return an array of zeros
        if k == 0:
            return [0] * n
        
        # Initialize the result array
        result = [0] * n
        
        if k > 0:
            for i in range(n):
                result[i] = sum(code[(i + j) % n] for j in range(1, k + 1))
        else:
            for i in range(n):
                result[i] = sum(code[(i + j) % n] for j in range(k, 0))
        
        return result

        