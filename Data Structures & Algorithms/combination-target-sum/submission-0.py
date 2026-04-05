class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # Brute force approach is keep going till you exceed the target
        res = []
        def backtrack(i, currSet, currSum):
            if i>= len(nums) or currSum>=target:
                if currSum==target:
                    res.append(currSet[:])
                return
            
            backtrack(i,currSet+[nums[i]], currSum+nums[i]) #include and stay
            backtrack(i+1,currSet, currSum) #exclude and move ahead

        backtrack(0,[],0)
        return res
        