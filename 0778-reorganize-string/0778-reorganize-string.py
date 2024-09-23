class Solution:
    def reorganizeString(self, s: str) -> str:
        # Step 1: Count the frequency of each character
        freq = Counter(s)

        # Step 2: Check if the solution is possible
        max_freq = max(freq.values())
        if max_freq > (len(s) + 1) // 2:
            return ""
        
        # Step 3: Use a max heap to arrange the characters
        # In Python, heapq is a min-heap by default, so we use negative values to simulate a max-heap
        heap = [(-count, char) for char, count in freq.items()]
        heapq.heapify(heap)

        ans = []
        prev_count, prev_char = 0, ''

        # Step 4: Greedy arrangement
        while heap:
            count, char = heapq.heappop(heap)
            ans.append(char)

            # If the previous character is still remaining, add it back to the heap
            if prev_count < 0:
                heapq.heappush(heap, (prev_count, prev_char))

            # Update the previous character and its count
            prev_count, prev_char = count + 1, char  # increment count since we used one occurrence of the char

        return "".join(ans)