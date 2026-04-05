class Solution:
    def rob(self, nums: List[int]) -> int:
        second_last_max, last_max = 0, 0

        for i in range(len(nums)):
            last_max, second_last_max = max(second_last_max + nums[i], last_max), last_max

        return max(last_max, second_last_max)


