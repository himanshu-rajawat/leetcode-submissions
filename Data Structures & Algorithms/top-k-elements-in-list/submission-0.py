import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # prepare a frequency counter -> o(n)
        # filter out top k -> o(n*k)   
        # overall time complexity -> o(n*k)

        # using heap
        # prepare a frequency counter -> o(n)
        # push all elements to heap -> o(nlogk)
        # getting top k frequent elements -> o(logk)
        # overall time complexity -> o(nlogk)

        # trying to make it in o(n)
        # creating frequency counter is all right
        # creating array of length n will help
        counter = {}

        for num in nums:
            counter[num] = counter.get(num, 0)+1
        
        heap = []
        for num in counter:
            heapq.heappush(heap,(counter[num], num))
            if len(heap)>k:
                heapq.heappop(heap)

        res = []
        while len(res)<k:
            res.append(heapq.heappop(heap)[1])
        
        return res



        