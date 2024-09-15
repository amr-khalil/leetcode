class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # xor cancel the duplications
        # a ^ b ^ c ^ b ^ c = a
        xor = 0
        for num in nums:
            xor ^= num
        return xor