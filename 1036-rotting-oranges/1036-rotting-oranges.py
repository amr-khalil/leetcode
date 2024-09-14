class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        fresh_oranges = 0
        # add the rotten oranges into a queue
        queue = collections.deque()
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))

                elif grid[r][c] == 1:
                    fresh_oranges += 1

        # If no fresh oranges, return 0 early.
        if fresh_oranges == 0:
            return 0

        directions = [(0,1), (1, 0), (0, -1), (-1, 0)]
        time = 0
        while queue:
            level_size = len(queue)
            for _ in range(level_size):
                r, c = queue.popleft()
                for x, y in directions:
                    nx = r + x
                    ny = c + y

                    # check if neighbours are fresh
                    if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 1:
                        grid[nx][ny] = 2 # make it rotten
                        queue.append((nx, ny)) # add to queue
                        fresh_oranges -= 1 # decrease fresh oranges

            # Only increment time if we processed any oranges in this level
            if queue:
                time += 1

        print(queue, fresh_oranges)
        return time if fresh_oranges == 0 else -1