class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        # selection sort
        max_val = max(nums)
        for i in range(len(nums)):
            min_num = max_val
            idx = i
            for j in range(i, len(nums)):
                if min_num>nums[j]:
                    idx = j
                    min_num = nums[j]
            nums[i], nums[idx] = nums[idx], nums[i]
        return nums
            
