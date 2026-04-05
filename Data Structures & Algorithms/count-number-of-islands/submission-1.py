class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        visited = set()
        ROW, COL = len(grid), len(grid[0])
        def bfs(i, j):
            q = deque()

            q.append((i,j))
            visited.add((i,j))

            while q:
                r,c= q.popleft()

                for dr,dc in [(0,1), (0,-1), (1,0), (-1,0)]:
                    r_, c_ = r+dr, c+dc

                    if 0<=r_<ROW and 0<=c_<COL and (r_, c_) not in visited and grid[r_][c_]=="1":
                        q.append((r_,c_))
                        visited.add((r_,c_))
        

        for i in range(ROW):
            for j in range(COL):
                if grid[i][j]=="1" and (i,j) not in visited:
                    bfs(i,j)
                    islands+=1
        
        return islands
        