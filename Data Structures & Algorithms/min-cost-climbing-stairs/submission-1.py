class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        last, second_last, n = cost[-1], 0, len(cost)

        for i in range(n-2, -1, -1):
            temp = last
            last = cost[i] + min(last, second_last)
            second_last = temp
        
        return min(last, second_last)
        