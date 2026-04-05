class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # permutation 
        state = [False for _ in nums]
        res = []
        def backtrack(perms, state):
            if len(perms)==len(nums):
                res.append(perms[:])
                return
            
            for i in range(len(nums)):
                if not state[i]:
                    perms.append(nums[i])
                    state[i]=True
                    backtrack(perms, state)
                    perms.pop()
                    state[i]=False
        backtrack([], state)
        return res

        
