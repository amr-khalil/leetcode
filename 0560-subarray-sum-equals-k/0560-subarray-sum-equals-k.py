class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        freq = defaultdict(int)  # Initialize a dictionary to store the frequency of prefix sums
        freq[0] = 1  # Base case: a sum of 0 is seen once (before any elements are added)
        count = 0  # This will store the number of subarrays that sum to k
        current = 0  # This will store the cumulative sum of the elements as we iterate through nums

        # Iterate over each number in the list
        for n in nums:
            current += n  # Update the current cumulative sum by adding the current number
            diff = current - k  # Calculate the difference needed to reach the target sum k
            if diff in freq:  # If the difference is in the dictionary, it means there's a subarray that sums to k
                count += freq[diff]  # Increment count by the number of times the difference has occurred
            freq[current] += 1  # Add/update the current sum in the dictionary
        
        return count  # Return the total count of subarrays that sum to k