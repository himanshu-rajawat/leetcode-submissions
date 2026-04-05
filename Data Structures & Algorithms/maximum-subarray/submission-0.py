class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # n3 for brute force
        # n2 optimised with two pointer
        # n with locally optimised approach

        curr, global_max = float("-inf"), float("-inf")

        for num in nums:
            curr = max(curr+num, num)
            global_max = max(curr, global_max)
        
        return global_max