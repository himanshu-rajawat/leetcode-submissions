class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        for i in range(len(points)):
            dis = (points[i][0])**2+(points[i][1])**2
            points[i]=[dis]+points[i]
        heapq.heapify(points)
        print(points)

        for _ in range(k):
            point = heapq.heappop(points)
            res.append([point[1],point[2]])
        
        return res