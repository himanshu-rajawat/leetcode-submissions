class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [False]*len(nums)
        dp[-1] = True

        for i in range(len(nums)-1, -1, -1):
            num = nums[i]
            curr = dp[i]
            for j in range(num+1):
                if (i+j)<len(nums) and dp[i+j]:
                    curr = True
            dp[i]=curr
        return dp[0]