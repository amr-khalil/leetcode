class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        rows, cols = len(rooms), len(rooms[0])
        queue = collections.deque()

        # add the gates into the queue
        for r in range(rows):
            for c in range(cols):
                if rooms[r][c] == 0:
                    queue.append((r, c))

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        # loop over the queue
        dst = 1
        while queue:
            level_size = len(queue)
            # loop over queue level
            for _ in range(level_size):
                r, c = queue.popleft()
                # loop over the directions, to check the neighbours
                for x, y in directions:
                    nx = r + x
                    ny = c + y
                    if 0 <= nx < rows and 0 <= ny < cols and rooms[nx][ny] == 2147483647:
                        rooms[nx][ny] = dst # add the distance to the room
                        queue.append((nx, ny)) # add the same room into the queue
            if queue:
                print(queue)
                dst += 1

