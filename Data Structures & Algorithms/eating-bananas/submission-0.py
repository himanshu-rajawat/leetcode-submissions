import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        min_val, max_val = 1, max(piles)
        res = -1

        def calculate_time(rate):
            time = 0
            for pile in piles:
                time += math.ceil(pile/rate)
            return time

        # binary search for rate
        while min_val <= max_val:
            rate = (min_val+max_val)//2
            time = calculate_time(rate)
            print(rate, time)

            if time <= h:
                res = rate
                max_val = rate-1
            else:
                min_val= rate+1

        return res
        