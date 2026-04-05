class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        cache = {}
        coins.sort()
        def dfs(amt, i):
            # base case
            if amt<0:
                return 0
            if amt==0:
                return 1
            if i>=len(coins):
                return 0
            if (amt,i) not in cache:
                comb = 0
                coin = coins[i]
                max_coin_num = amt//coin
                for j in range(max_coin_num):
                    comb+=dfs(amt-(j+1)*coin,i+1)
                comb+=dfs(amt,i+1)
                cache[(amt,i)] = comb
            return cache[(amt,i)]
        return dfs(amount,0)