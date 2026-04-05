class Solution:
    def rob(self, nums: List[int]) -> int:
        # the extra contraint here is that if you rob the first house last one is not allowed
        def rob_house_in_line(startIndex, endIndex):
            h1, h2 = 0, 0
            if startIndex>endIndex:
                return nums[0]
            for i in range(startIndex, endIndex+1):
                temp = max(nums[i]+h1, h2)
                h1 = h2
                h2 = temp
            return max(h1, h2)
        lastIdx = len(nums)-1
        return max(rob_house_in_line(0,lastIdx-1), rob_house_in_line(1,lastIdx))
        