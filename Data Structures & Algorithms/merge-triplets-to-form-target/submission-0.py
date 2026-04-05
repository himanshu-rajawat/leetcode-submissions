class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        tar1, tar2, tar3 = target[0], target[1], target[2]
        maxt1, maxt2, maxt3 = float("-inf"), float("-inf"), float("-inf")

        for t in triplets:
            t1, t2, t3 = t[0], t[1], t[2]
            if (t1<= tar1 and  t2<= tar2 and t3<= tar3) and (t1== tar1 or  t2== tar2 or t3== tar3)  :
                maxt1, maxt2, maxt3 = max(maxt1, t1), max(maxt2, t2), max(maxt3, t3)
        
        return maxt1==tar1 and maxt2==tar2 and maxt3==tar3