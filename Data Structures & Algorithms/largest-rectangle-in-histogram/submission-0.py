class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # idea is to focus on left and right limits till we can extend the bar
        n = len(heights)

        # finding right limits
        right_limits = [n-1 for _ in range(n)]
        stack_r = []

        for i in range(n):
            height = heights[i]
            while stack_r and stack_r[-1][0]>height:
                data = stack_r.pop()
                right_limits[data[1]] = i-1
            stack_r.append([height,i])

        # finding left limits
        left_limits = [0 for _ in range(n)]
        stack_l = []

        for i in range(n-1,-1,-1):
            height = heights[i]
            while stack_l and stack_l[-1][0]>height:
                data = stack_l.pop()
                left_limits[data[1]] = i+1
            stack_l.append([height,i])
        
        # calculating max_area
        max_area = 0

        for i in range(n):
            max_area = max(max_area, (right_limits[i]-left_limits[i]+1)*heights[i])
        return max_area