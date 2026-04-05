class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal_idx = len(nums)-1

        for i in range(len(nums)-1, -1, -1):
            num = nums[i]
            if i+num>=goal_idx:
                print(goal_idx)
                goal_idx = i
        return goal_idx ==0