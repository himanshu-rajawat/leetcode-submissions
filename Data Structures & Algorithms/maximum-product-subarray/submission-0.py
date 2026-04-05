class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # key is to use a locally optimal approach here, that if res is lesser than current ele, start new array, but the catch are negative numbers so need to keep both max and min
        curr_max_product = 1
        curr_min_product = 1
        max_product = float("-inf")

        for i in range(len(nums)):
            curr = nums[i]
            temp = curr_max_product*curr
            # max
            curr_max_product = max(curr_max_product*curr, curr, curr_min_product*curr)
            # min
            curr_min_product = min(curr_min_product*curr, curr, temp)
            max_product = max(max_product, curr_max_product)
        return max_product