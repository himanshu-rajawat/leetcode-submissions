from collections import deque
from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[str]]) -> int:
        visited = set()
        max_area = 0

        def bfs(row, col):
            queue = deque([[row, col]])
            visited.add((row, col))  # Mark as visited when adding to the queue
            area = 0

            while queue:
                r, c = queue.popleft()  # FIFO for BFS
                area+=1
                for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nr, nc = r + dr, c + dc
                    if (
                        0 <= nr < len(grid) and  # Check row bounds
                        0 <= nc < len(grid[0]) and  # Check column bounds
                        (nr, nc) not in visited and  # Not visited
                        grid[nr][nc] == 1  # Is land
                    ):
                        visited.add((nr, nc))  # Mark as visited
                        queue.append([nr, nc])  # Add to queue
            return area

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and (i, j) not in visited:
                    max_area = max(bfs(i, j), max_area)
        return max_area
