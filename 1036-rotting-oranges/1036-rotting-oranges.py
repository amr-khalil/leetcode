class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        queue = deque()
        fresh_oranges = 0

        # Initialize the queue with all rotten oranges and count fresh oranges.
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh_oranges += 1
        
        # If there are no fresh oranges, return 0 minutes.
        if fresh_oranges == 0:
            return 0
        
        # Directions for 4-directional adjacency.
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        minutes_passed = -1
        # BFS starts with all rotten oranges in the queue.
        while queue:
            minutes_passed += 1
            for _ in range(len(queue)):
                x, y = queue.popleft()
                # Check all 4-directionally adjacent cells.
                for dx, dy in directions:
                    nx = x + dx
                    ny = y + dy

                    if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 1:
                        # Rot the fresh orange and add it to the queue.
                        grid[nx][ny] = 2
                        queue.append((nx, ny))
                        fresh_oranges -= 1

            print(queue, fresh_oranges)

        # If there are still fresh oranges, return -1.
        return minutes_passed if fresh_oranges == 0 else -1