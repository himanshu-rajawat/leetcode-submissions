class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if not stones:
            return 0

        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones)>1:
            x = heapq.heappop(stones)
            y = heapq.heappop(stones)

            diff = abs(y-x)

            print(len(stones), x, y, diff)

            if diff:
                heapq.heappush(stones, -diff)

        return abs(stones[0]) if stones else 0
        

