class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # n3 for brute force
        # n2 optimised with two pointer
        # n with locally optimised approach

        curr, max_sum =0, float("-inf")

        for num in nums:
            curr+=num
            max_sum = max(max_sum, curr)
            if curr<0:
                curr = 0
        return max_sum
        