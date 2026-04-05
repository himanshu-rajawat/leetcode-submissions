class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        sides = [0, 0, 0, 0]
        res = False
        if sum(matchsticks)%4!=0:
            return res
        matchsticks.sort(reverse=True)
        max_side = sum(matchsticks)//4

        def backtrack(i):
            nonlocal res
            if i>=len(matchsticks):
                if len(set(sides))==1:
                    res = True
                return
            
            for j in range(len(sides)):
                if sides[j]+matchsticks[i]<= max_side:
                    sides[j]+=matchsticks[i]
                    backtrack(i+1)
                    sides[j]-=matchsticks[i]
        backtrack(0)
        return res