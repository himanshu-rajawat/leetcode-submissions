class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        # bubble sort
        flag = True
        while flag:
            flag = False
            for i in range(1, len(nums)):
                if nums[i]<nums[i-1]:
                    flag = True
                    nums[i], nums[i-1] = nums[i-1], nums[i]
        return nums
        