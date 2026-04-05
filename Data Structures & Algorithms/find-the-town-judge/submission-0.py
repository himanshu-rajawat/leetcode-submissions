class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n==1:
            return 1
        adj_list = {}
        out_adj_list = {}

        for edge in trust:
            a, b = edge[0], edge[1]

            adj_list[b]=adj_list.get(b,0)+1
            out_adj_list[a] = adj_list.get(a,0)+1

        for person in adj_list:
            if adj_list[person]==(n-1) and person not in out_adj_list:
                return person
        return -1
        