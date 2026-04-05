class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        n = len(nums)

        def backtrack(i, subSet):
            # base cases
            if i >= n:
                res.append(subSet)
                return
            # case when you select curr
            backtrack(i+1, subSet+[nums[i]])

            # case when you drop current
            while i+1<n and nums[i]==nums[i+1]:
                i+=1
            backtrack(i+1, subSet)
        
        backtrack(0,[])
        return res

        