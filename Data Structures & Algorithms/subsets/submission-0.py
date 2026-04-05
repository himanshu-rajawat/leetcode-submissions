class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def backtrack(idx, currList):
            print(idx, currList)
            if idx>len(nums)-1:
                res.append(currList)
                return
            
            backtrack(idx+1,currList) #skipping current index ele
            backtrack(idx + 1, currList + [nums[idx]])  # Adding current element
        backtrack(0,[])
        return res