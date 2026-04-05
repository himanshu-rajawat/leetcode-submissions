class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = {}
        count = 0

        def bfs(row, col, visited, grid):
            queue = [[row,col]]
            while queue:
                pos = queue.pop()
                r,c = pos[0], pos[1]
                visited[(r,c)] = True

                if r-1>=0 and (r-1,c) not in visited and grid[r-1][c]=="1":
                    queue.append([r-1,c])
                if r+1<len(grid) and (r+1,c) not in visited and grid[r+1][c]=="1":
                    queue.append([r+1,c])
                if c-1>=0 and (r,c-1) not in visited and grid[r][c-1]=="1":
                    queue.append([r,c-1])
                if c+1<len(grid[0]) and (r,c+1) not in visited and grid[r][c+1]=="1":
                    queue.append([r,c+1])


        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=="1" and (i,j) not in visited:
                    bfs(i,j,visited, grid)
                    count+=1
        return count
        