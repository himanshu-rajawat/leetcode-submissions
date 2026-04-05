class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # permutation 
        nums.sort()
        state = {}
        for num in nums:
            state[num] = state.get(num, 0)+1
        res = []
        def backtrack(perms, state):
            if len(perms)==len(nums):
                res.append(perms[:])
                return
            
            for num in state:
                if state[num]>0:
                    perms.append(num)
                    state[num] = state.get(num)-1
                    backtrack(perms, state)
                    perms.pop()
                    state[num] = state.get(num, 0)+1
        backtrack([], state)
        return res

        
