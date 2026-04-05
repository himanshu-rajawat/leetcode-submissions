class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        max_val = len(grid)+len(grid[0])+1
        ROW, COL = len(grid), len(grid[0])
        INF = 2147483647

        q = deque()
        visited = set()

        for i in range(ROW):
            for j in range(COL):
                if grid[i][j]==0:
                    q.append((i,j,1))
                    visited.add((i,j))
        
        while q:
            r, c, dist = q.popleft()

            for dr, dc in [(0,1), (1,0), (-1,0), (0,-1)]:
                r_, c_ = r+dr, c+dc
                if 0<=r_<ROW and 0<=c_<COL and (grid[r_][c_]!=-1 and grid[r_][c_]!=0) and (r_,c_) not in visited:
                    grid[r_][c_]=dist
                    q.append((r_,c_, dist+1))
                    visited.add((r_,c_))

