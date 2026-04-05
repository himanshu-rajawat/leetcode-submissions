from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # try the same usign a queue to each time we see an element greater than current we push that to queue

        q = deque()
        max_ele = []

        for i in range(len(nums)):
            num = nums[i]
            while q and q[-1][0] <num:
                q.pop()
            q.append((num,i))

            while q[0][1] <= i-k:
                q.popleft()
            
            if i >= k-1:
                max_ele.append(q[0][0])
        return max_ele

        