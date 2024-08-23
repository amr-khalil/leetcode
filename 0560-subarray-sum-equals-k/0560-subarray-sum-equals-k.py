class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # only postive intergers
        prefix = defaultdict(int)
        prefix[0] = 1

        current = 0
        count = 0

        for num in nums:
            current += num

            if (current - k) in prefix:
                count += prefix[current-k]
            
            prefix[current] += 1


        return count
