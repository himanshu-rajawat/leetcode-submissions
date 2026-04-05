class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        first, second, n = cost[0], cost[1], len(cost)

        for i in range(2, n):
            curr = cost[i]
            min_cost_curr = min(first+curr, second+curr)
            print("min cost for",i,min_cost_curr,first,second)
            first = second
            second = min_cost_curr
        
        return min(first, second)
        