class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(cost)>sum(gas):
            return -1
        net_cost_arr = [gas[i]-cost[i] for i in range(len(gas))]

        curr_sum = 0
        res = 0

        for i in range(len(net_cost_arr)):
            c = net_cost_arr[i]
            curr_sum+= c
            if curr_sum<0:
                curr_sum = 0
                res = i+1
        
        return res if res<len(gas) else -1