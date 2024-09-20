class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        # Find the longest continuous sub array that has exactly 2 distinct elements.
        n = len(fruits)
        l = 0
        max_fruits = 0
        freq = defaultdict(int) # Dictionary to count the frequency of each type of fruit in the current window.

        for r in range(n):
            freq[fruits[r]] += 1

            # Shrink the window if there are more than 2 distinct fruits
            if len(freq) > 2:
                freq[fruits[l]] -= 1 # Decrease the count of the fruit at the left pointer.
                # Remove when count is zero: If the count of a particular fruit type reaches zero, it means that fruit is no longer part of the window 
                if freq[fruits[l]] == 0:
                    del freq[fruits[l]]
                l += 1

            winSize = r - l + 1
            max_fruits = max(max_fruits, winSize)

        return max_fruits

