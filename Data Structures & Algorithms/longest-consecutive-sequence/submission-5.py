class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        res, curr = 0, 0
        print(nums_set)
        for num in nums:
            curr+=1
            curr_num = num
            while curr_num+1 in nums_set:
                curr+=1
                nums_set.remove(curr_num+1)
                curr_num +=1
            curr_num = num
            while curr_num-1 in nums_set:
                curr+=1
                nums_set.remove(curr_num-1)
                curr_num -=1
            res = max(res, curr)
            curr=0
        return res
        