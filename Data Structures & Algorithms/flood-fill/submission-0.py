class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m, n = len(image), len(image[0])
        start_color = image[sr][sc]
        if start_color==color:
            return image
        visited  = set()
        directions = [(0,1), (1,0), (-1,0), (0,-1)]

        def bfs(i, j):
            q = deque()
            q.append((i, j))
            image[i][j] = color
            while q:
                pr, pc = q.popleft()
                for dr, dc in directions:
                    pr_new, px_new = pr+dr, pc+dc
                    if (0<=pr_new<m and 0<=px_new<n) and image[pr_new][px_new] != color  and image[pr_new][px_new]==start_color:
                        q.append((pr_new, px_new))
                        image[pr_new][px_new] = color
        
        bfs(sr,sc)
        return image