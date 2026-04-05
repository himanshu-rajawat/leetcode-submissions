class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero, two = 0, len(nums)-1

        i = 0
        while i<=two:
            num = nums[i]

            if num == 0:
                nums[zero], nums[i] = nums[i], nums[zero]
                zero+=1
            
            if num == 2:
                nums[two], nums[i] = nums[i], nums[two]
                two-=1
                i-=1
        
            i+=1        

        
        