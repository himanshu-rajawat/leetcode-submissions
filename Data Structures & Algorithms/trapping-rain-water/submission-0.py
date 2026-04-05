class Solution:
    def trap(self, height: List[int]) -> int:
        #solution can be found by thinking on how much water we can store on each height level
        # will calculate max_left_height and max_right_height to each level
        # and then amount by which min of these two heights is greater than height at that level (if it is greater), that will be units of water stored (or area)

        #caculating max_left_heights
        max_left_heights = [0 for _ in range(len(height))]
        max_height = 0
        for i in range(len(height)):
            max_left_heights[i] = max_height
            max_height = max(height[i], max_height)

        #caculating max_right_heights
        max_right_heights = [0 for _ in range(len(height))]
        max_height = 0
        for i in range(len(height)-1, -1, -1):
            max_right_heights[i] = max_height
            max_height = max(height[i], max_height)

        #calculating total area
        area = 0
        for i in range(len(height)):
            water_area = min(max_left_heights[i], max_right_heights[i]) - height[i]
            if water_area>0:
                area+=water_area
        return area

        