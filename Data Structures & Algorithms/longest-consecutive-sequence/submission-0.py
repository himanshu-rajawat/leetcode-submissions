class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #sets have look up time o(1), read more about that
        nums_set = set(nums)
        max_count = 0
        for num in nums:
            if num in nums_set:
                count = 1
                pre, nex = num-1, num+1
                while pre in nums_set:
                    nums_set.remove(pre)
                    count+=1
                    pre -=1
                while nex in nums_set:
                    nums_set.remove(nex)
                    count+=1
                    nex +=1
                nums_set.remove(num)
                max_count = max(max_count, count)
        return max_count