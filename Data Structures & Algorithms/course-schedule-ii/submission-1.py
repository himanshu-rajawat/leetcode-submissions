class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {num:[] for num in range(numCourses)}
        for data in prerequisites:
            adj[data[0]].append(data[1])
        output = []
        visited = set()
        output_set = set()
        cycle = False
        def dfs(course):
            nonlocal cycle
            print(course,visited)
            if not adj[course]:
                if course not in output_set:
                    output.append(course)
                    output_set.add(course)
                return
            if course in visited:
                cycle = True
                return
            visited.add(course)
            for pre_course in adj[course]:
                dfs(pre_course)
            adj[course] = []
            output.append(course)
            output_set.add(course)
            visited.remove(course)
        
        for num in range(numCourses):
            dfs(num)
            if cycle: return []
        return output