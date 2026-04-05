from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # idea is to do a bfs on a 'o' and mark its region as X if it is surrounded by 'X'
        visited = set()
        rows, cols = len(board), len(board[0])

        def bfs(i,j):
            region = []
            queue = deque()
            queue.append((i,j))
            is_surrounded = True

            while queue:
                row, col = queue.popleft()
                visited.add((row,col))
                region.append([row,col])
                if row == 0 or row == rows-1 or col == 0 or col==cols-1:
                            is_surrounded = False
                
                for dr, dc in [[1,0],[0,1],[-1,0],[0,-1]]:
                    n_row, n_col = row+dr,col+dc
                    if 0<= n_row<rows and 0<=n_col<cols and (n_row, n_col) not in visited and board[n_row][n_col]=='O':
                        queue.append((n_row, n_col))
            if is_surrounded:
                for point in region:
                    i,j = point[0], point[1]
                    board[i][j] = 'X'


        for i in range(rows):
            for j in range(cols):
                if board[i][j]=='O' and (i,j) not in visited:
                    bfs(i,j)
        