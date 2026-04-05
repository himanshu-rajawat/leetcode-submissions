class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # I think this is a cycle detection problem, which will be solved in two parts and end goal is to find the start of the cycle

        slow, fast = 0, 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        slow2 = 0

        while True:
            slow = nums[slow]
            slow2= nums[slow2]
            if slow2==slow:
                return slow