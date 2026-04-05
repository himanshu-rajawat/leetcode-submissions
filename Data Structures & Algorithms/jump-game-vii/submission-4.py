from collections import deque
class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        if s[n-1] == '1':
            return False
        
        q = deque()
        last_idx = 0
        q.append(0)

        while q:
            idx = q.popleft()
            for j in range(max(idx+minJump, last_idx+1), min(n, maxJump+idx+1)):
                if s[j] == '0':
                        if j == n - 1:
                            return True
                        q.append(j)
            last_idx = max(last_idx, idx + maxJump)
        return False