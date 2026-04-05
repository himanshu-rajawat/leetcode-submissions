class MedianFinder:

    def __init__(self):
        self.arr = []
        self.heap = []

    def addNum(self, num: int) -> None:
        self.arr.append(num)
        heapq.heappush(self.heap, num)
        

    def findMedian(self) -> float:
        is_odd = len(self.arr)%2==1
        popped_ele = []
        median = None

        if is_odd:
            m = (len(self.arr)//2)+1
            while m:
                median = heapq.heappop(self.heap)
                popped_ele.append(median)
                m-=1
            for num in popped_ele:
                heapq.heappush(self.heap, num)
        else:
            m = (len(self.arr)//2)
            n = None
            while m:
                n = heapq.heappop(self.heap)
                popped_ele.append(n)
                m-=1

            n2 = heapq.heappop(self.heap)
            popped_ele.append(n2)
            median = (n+n2)/2

            for num in popped_ele:
                heapq.heappush(self.heap, num)

        return median