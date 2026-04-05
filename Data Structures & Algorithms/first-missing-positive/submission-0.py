class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()

        i, check = 0, 1

        while i<len(nums):
            num = nums[i]
            print(i, num, check)

            if num>0 and num!=check:
                return check
            elif num==check:
                while i+1<len(nums) and nums[i]==check:
                    i+=1
                check+=1
            else:
                i+=1
        return check
