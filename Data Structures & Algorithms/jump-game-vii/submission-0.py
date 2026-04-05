class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        if s[n-1] == '1':
            return False
        
        dp = [False for _ in range(n)]
        dp[-1] = True

        for i in range(n-1, -1, -1):
            if s[i]=='0':
                for j in range(i+1, n):
                    if dp[j] and minJump<=j-i<=maxJump:
                        dp[i]=True
        return dp[0]==True