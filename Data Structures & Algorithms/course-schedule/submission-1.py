from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # do dfs and check if the curr course has already been seen, if yes there is a cycle and this we can not finish the courses
        
        # create an adjancency list first
        adj_list = {num:[] for num in range(numCourses)}

        for prerequisite in prerequisites:
            course, prerequisitesCourse = prerequisite[0], prerequisite[1]
            adj_list[course].append(prerequisitesCourse)
        
        # dfs on adj list
        visited = set()

        def dfs(course):
            if course in visited:
                return False
            pre_courses = adj_list[course]
            if not pre_courses:
                return True
            
            visited.add(course)
            for pre in pre_courses:
                if not dfs(pre): return False
            adj_list[course]=[]
            visited.remove(course)
            return True

        for course in range(numCourses):
            if not dfs(course): return False
        return True
        