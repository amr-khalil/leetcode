class Solution:
    def largestInteger(self, num: int) -> int:
        num = [int(n) for n in str(num)]
        even = [-n for n in num if n % 2 == 0]
        odd = [-n for n in num if n % 2 == 1]

        heapify(odd)
        heapify(even)

        ans = 0
        for n in num:
            if n % 2 == 0:
                ans = ans * 10 - heappop(even)
            else:
                ans = ans * 10 - heappop(odd)

        return ans