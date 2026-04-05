class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff_store = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in diff_store:
                return [diff_store[diff], i]
            diff_store[nums[i]] = i
        return -1

        