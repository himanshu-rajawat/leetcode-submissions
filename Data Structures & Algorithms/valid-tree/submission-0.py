class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # idea is to traverse graph from 0 do a dfs, and we should not encounter any cycles and size of visited should be equal to n
        adj = {num:[] for num in range(n)}
        for node1, node2 in edges:
            adj[node1].append(node2)
            adj[node2].append(node1)
        
        visited = set()
        cycle = False
        def dfs(node, parent):
            nonlocal cycle
            if node in visited:
                cycle = True
            else:
                visited.add(node)
                for nbr in adj[node]:
                    if nbr != parent:
                        dfs(nbr, node)

        dfs(0, None)
        return len(visited)==n and not cycle
                

        