from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # try the same usign a queue to each time we see an element greater than current we push that to queue

        q = deque()
        l = 0
        max_ele = []

        for r in range(len(nums)):
            # Step 1: Remove Out-of-Window Elements
            while q and r>k-1 and q[0]<=r-k:
                q.popleft()
            
            # Step 2: Maintain Monotonic Decreasing Order
            while q and nums[q[-1]]<nums[r]:
                q.pop()

            # Step 3: Add Current Index
            q.append(r)

            # Step 4: Record the Maximum
            if r>=k-1:
                max_ele.append(nums[q[0]])


            
        return max_ele

        