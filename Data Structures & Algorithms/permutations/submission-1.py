class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums)==0:
            return [[]]
        res = []
        perms = self.permute(nums[1:])
        curr = nums[0]

        for p in perms:
            for i in range(len(p)+1):
                p_copy = p.copy()
                p_copy.insert(i, curr)
                res.append(p_copy)
        return res
