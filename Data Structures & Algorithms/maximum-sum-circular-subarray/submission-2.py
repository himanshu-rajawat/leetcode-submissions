class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        curr, max_sum = 0, float("-inf")
        curr_min, min_sum = 0, float("inf")

        for i in range(len(nums)):
            curr+=nums[i]
            curr_min+=nums[i]
            max_sum = max(max_sum, curr)
            min_sum = min(min_sum, curr_min)
            if curr<0:
                curr=0
            if curr_min>0:
                curr_min=0
        return max(max_sum, sum(nums)-min_sum if sum(nums)>min_sum else float("-inf") )
        