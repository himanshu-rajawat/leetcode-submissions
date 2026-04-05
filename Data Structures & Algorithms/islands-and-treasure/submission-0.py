from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        row, col = len(grid), len(grid[0])

        # bfs that will add entries in grid
        def bfs(r,c):
            queue = deque()
            queue.append((r,c,0))
            visited = set()

            while queue:
                r_curr, c_curr, dis = queue.popleft()
                visited.add((r_curr,c_curr))
                grid[r_curr][c_curr] = min(grid[r_curr][c_curr], dis) if grid[r_curr][c_curr]>0 else dis

                for dr, dc in [[1,0],[0,1],[-1,0],[0,-1]]:
                    n_row, n_col = r_curr+dr, c_curr+dc
                    if 0<=n_row<row and 0<=n_col<col and (n_row,n_col) not in visited:
                        if grid[n_row][n_col] > 0:
                            queue.append((n_row, n_col, dis+1))


        # traverse grid
        for r in range(row):
            for c in range(col):
                if grid[r][c]==0:
                    bfs(r,c)
        