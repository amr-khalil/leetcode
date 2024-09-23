class Solution:
    def reorganizeString(self, s: str) -> str:
        ans = []
        freq = Counter(s)
        pq = [(-count, char) for char, count in freq.items()]
        heapify(pq)

        while pq:
            c1, char1 = heappop(pq)
            if not ans or ans[-1] != char1:
                ans.append(char1)
                if c1 + 1 != 0:
                    heappush(pq, (c1 + 1, char1))
            
            else:
                if not pq:
                    return ''
                c2, char2 = heappop(pq)
                ans.append(char2)
                if c2 + 1 != 0:
                    heappush(pq, (c2+1, char2))
                heappush(pq, (c1, char1))
        
        return ''.join(ans)