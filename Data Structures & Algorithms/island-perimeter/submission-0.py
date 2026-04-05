class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        df = [(0,1), (1,0), (-1,0), (0, -1)]
        res = 0
        
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c]==1:
                    for dr, dc in df:
                        rn, cn = r+dr, c+dc
                        if not ((0<=rn<ROW and 0<=cn<COL) and grid[rn][cn]==1):
                            res+=1
        return res

        