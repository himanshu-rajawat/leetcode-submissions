class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        curr, last = 0, None
        count = 0
        for num in nums:
            if (last==None or last!=num):
                nums[curr] = num
                count+=1
                curr+=1
            last = num
        return count