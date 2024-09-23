class Solution:
    def reorganizeString(self, s: str) -> str:
        ans = []  # Initialize an empty list to store the result
        # Create a list of tuples (negative count, character) for each unique character in the string
        # Negative count is used so the heap can function as a max-heap
        pq = [(-count, char) for char, count in Counter(s).items()]
        heapify(pq)  # Transform the list into a heap (min-heap in Python, but we use negative values for max-heap behavior)

        # Process the heap until it's empty
        while pq:
            c1, ch1 = heappop(pq)  # Pop the character with the highest count (due to negative values, this is the "max" character)
            
            # If the result list is empty or the last added character is different from the current one
            if not ans or ch1 != ans[-1]:
                ans.append(ch1)  # Add the current character to the result list
                # If there are more occurrences of this character, reinsert it into the heap with the updated count
                if c1 + 1 != 0: 
                    heappush(pq, (c1 + 1, ch1))  # Increment the count since it's negative and push back to the heap
            else:
                # If the top character is the same as the last character in the result, we need to use a different character
                if not pq:  # If there's no other character available, it's impossible to reorganize the string
                    return ''
                c2, ch2 = heappop(pq)  # Pop the next most frequent character
                ans.append(ch2)  # Add it to the result
                # If there are more occurrences of this second character, reinsert it with the updated count
                if c2 + 1 != 0:
                    heappush(pq, (c2 + 1, ch2))  # Increment the count and push it back to the heap
                heappush(pq, (c1, ch1))  # Push the original character back into the heap since we couldn't use it this round

        return ''.join(ans)  # Convert the list of characters back to a string and return the result
