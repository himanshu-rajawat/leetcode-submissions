class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1

        # binary search
        while l<=r:
            m = (l+r)//2

            # return if found
            if nums[m]==target:
                return m
            elif nums[m]>target: # target lies in left search space
                r -=1
            else:   #target lies in right seach space
                l +=1
        
        return -1 #return -1 when no result is found

        