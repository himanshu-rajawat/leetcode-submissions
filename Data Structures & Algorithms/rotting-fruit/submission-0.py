class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        fresh_fruits = set()
        q = deque()
        total_time = 0

        for i in range(ROW):
            for j in range(COL):
                if grid[i][j]==1:
                    fresh_fruits.add((i,j))
                if grid[i][j]==2:
                    q.append((i,j,0))
        
        while q:
            r, c, time = q.popleft()

            for dr, dc in [(0,1), (0,-1), (1,0), (-1,0)]:
                r_, c_ = r+dr, c+dc

                if (r_,c_) in fresh_fruits:
                    total_time = time+1
                    q.append((r_,c_,time+1))
                    fresh_fruits.remove((r_,c_))
        return total_time if len(fresh_fruits)==0 else -1
        

        
        
        