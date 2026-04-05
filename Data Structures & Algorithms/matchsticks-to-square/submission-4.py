class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        sides = [0, 0, 0, 0]
        if sum(matchsticks)%4!=0:
            return False
        matchsticks.sort(reverse=True)
        max_side = sum(matchsticks)//4

        def backtrack(i):
            if i>=len(matchsticks):
                if len(set(sides))==1:
                    return True
            
            for j in range(len(sides)):
                if sides[j]+matchsticks[i]<= max_side:
                    sides[j]+=matchsticks[i]
                    if backtrack(i+1):
                        return True
                    sides[j]-=matchsticks[i]
            return False
        return backtrack(0)