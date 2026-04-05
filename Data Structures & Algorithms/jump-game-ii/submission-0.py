class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [(False,0) for _ in range(len(nums))]
        dp[-1]=(True,0)

        for i in range(len(nums)-1, -1, -1):
            num = nums[i]
            for j in range(num+1):
                if i+j<len(nums) and dp[i+j][0]:
                    if dp[i][0]:
                        dp[i] = (True, min(1+dp[i+j][1], dp[i][1]))
                    else:
                        dp[i] = (True, 1+dp[i+j][1])
        return dp[0][1]