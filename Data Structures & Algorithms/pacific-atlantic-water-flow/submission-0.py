from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        res = []
        ROW, COL = len(heights), len(heights[0])

        p_set = set()
        a_set = set()

        def bfs(points, is_p):
            queue = deque()
            for point in points:
                r,c = point
                queue.append((r,c))

            while queue:
                for _ in range(len(queue)):
                    row, col = queue.popleft()
                    height = heights[row][col]

                    if is_p:
                        p_set.add((row,col))
                    else:
                        a_set.add((row,col))

                    for dr, dc in [[1,0],[0,1],[-1,0],[0,-1]]:
                        n_row, n_col = row+dr, col+dc
                        already_visited = (is_p and (n_row,n_col) in p_set) or (not is_p and (n_row,n_col) in a_set)
                        if 0<=n_row<ROW and 0<=n_col<COL and heights[n_row][n_col]>=height and not already_visited:
                            queue.append((n_row,n_col))

        pacific_ocean_points = []
        atlantic_ocean_points = []
        for r in range(ROW):
            pacific_ocean_points.append((r,0))
            atlantic_ocean_points.append((r,COL-1))
        for c in range(COL):
            pacific_ocean_points.append((0,c))
            atlantic_ocean_points.append((ROW-1,c))

        bfs(pacific_ocean_points, True)
        bfs(atlantic_ocean_points, False)
        
        return list(p_set.intersection(a_set))
