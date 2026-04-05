class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curr_max, curr_min, max_sum = None, None, float("-inf")
        for i in range(len(nums)):
            print(max_sum, curr_max, curr_min)
            curr = nums[i]
            curr_max, curr_min = max(curr_max*curr if curr_max!=None else curr, curr_min*curr if curr_min!=None else curr, curr), min(curr_max*curr if curr_max!=None else curr, curr_min*curr if curr_min!=None else curr, curr)
            max_sum = max(curr_max, max_sum)
        
        return max_sum