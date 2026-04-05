import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        arr = [[] for _ in range(len(nums))]

        for num in nums:
            counter[num] = counter.get(num, 0)+1
        
        
        for num in counter:
            arr[counter[num]-1].append(num)
        

        res = []
        while arr and len(res)<k:
            num = arr.pop()
            while len(num)>0 and len(res)<k:
                res.append(num.pop())
        
        return res