class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # Brute force approach is keep going till you exceed the target
        res = []

        def dfs(i, curr, curr_sum):
            if curr_sum> target:
                return
            if curr_sum==target:
                res.append(curr[:])
                return
            
            if i>=len(nums):
                if curr_sum==target:
                    res.append(curr[:])
                return
            
            # include
            curr.append(nums[i])
            dfs(i, curr, curr_sum+nums[i])

            # not include (backtrack)
            curr.pop()
            dfs(i+1, curr, curr_sum)
        
        dfs(0, [], 0)

        return res
        