class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        holding = None
        profit = 0
        for price in prices:
            if holding!=None and price-holding>0:
                profit+= (price-holding)
            holding = price

        return profit
            