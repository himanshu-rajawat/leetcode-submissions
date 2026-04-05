class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Number of coins will not be greater than amount
        cache = {}
        
        def dp(amount):
            if amount == 0:
                return 0
            if amount<0:
                return float("inf")
            if amount not in cache:
                min_coins = float("inf")
                for coin in coins:
                    min_coins = min(min_coins, 1+dp(amount-coin))
                cache[amount] = min_coins
            return cache[amount]

            return cache[amount]
        count = dp(amount)
        return count if count!=None and count<=amount else -1