class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cache = {}
        def dfs(i, allowed_ops):
            max_val = float("-inf")
            sell_itr = "s" in allowed_ops
            buy_itr = "b" in allowed_ops
            itr = "b" if buy_itr else ("s" if sell_itr else "cd")
            if i == len(prices)-1:
                if "s" in allowed_ops:
                    return prices[i]
                return 0
            
            if (i,itr) not in cache:
                if sell_itr:
                    max_val = max(max_val, prices[i]+dfs(i+1,["cd"]), dfs(i+1,["cd","s"]))
                elif allowed_ops==["cd"]:
                    max_val = max(max_val, dfs(i+1,["cd","b"]))
                else:
                    max_val = max(max_val, -prices[i]+dfs(i+1,["cd","s"]), dfs(i+1,["cd","b"]))
                cache[(i,itr)] = max_val
            # print(i, sell_itr, cache[(i,sell_itr)])
            return cache[(i,itr)]
        return dfs(0,["b","cd"])
        


        