class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])

        def backtrack(i, j, idx, visited):
            res = False
            if idx==len(word)-1:
                return True if word[idx]==board[i][j] else False
            
            valid_neighbour = get_valid_neighbour(i, j, word[idx+1], visited)

            visited.add((i,j))
            for n in valid_neighbour:
                i_new, j_new = n
                res = res or backtrack(i_new, j_new, idx+1, visited)
                if res:
                    break
            visited.remove((i,j))
            return res
            
        def get_valid_neighbour(i, j, char, visited):
            diff = [(1,0),(0,1),(-1,0),(0,-1)]
            res = []

            for df in diff:
                di, dj = df
                new_i, new_j = i+di, j+dj
                if 0<=new_i<m and 0<=new_j<n and board[new_i][new_j]==char and (new_i, new_j) not in visited:
                    res.append((new_i, new_j))
            return res
        
        for i in range(m):
            for j in range(n):
                if board[i][j]==word[0]:
                    if backtrack(i, j, 0, set()):
                        return True
        return False
        