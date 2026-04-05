class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # build an adjacency list
        adj = {num:[] for num in range(n)}
        for node1, node2 in edges:
            adj[node1].append(node2)
            adj[node2].append(node1)
        visited = set()
        component_count = 0
        def dfs(node, prev):
            if node not in visited:
                visited.add(node)

                for nbr in adj[node]:
                    if nbr != prev:
                        dfs(nbr, node)
        
        for node in range(n):
            if node not in visited:
                component_count+=1
                dfs(node, None)
        return component_count


        