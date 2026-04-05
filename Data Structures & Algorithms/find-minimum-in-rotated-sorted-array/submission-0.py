class Solution:
    def findMin(self, nums: List[int]) -> int:
        start, end = 0, len(nums)-1

        while nums[start]>nums[end]:
            mid = (start+end)//2

            if nums[end]<nums[mid]:
                start=mid+1 #min is in the right half
            else:
                end = mid #min is in the left half or mid
            
        return nums[start]
        