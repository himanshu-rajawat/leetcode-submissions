class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        heap = []
        counter= {}
        res=0
        for task in tasks:
            counter[task]=counter.get(task,0)+1
        
        for task in counter:
            heapq.heappush(heap,(-counter[task], task))

        while heap and sum(counter.values())>0:
            task_list = []
            for _ in range(n+1):
                if sum(counter.values())==0:
                    break
                else:
                    res+=1

                if heap:
                    ele = heapq.heappop(heap)
                    task = ele[1]
                    counter[task] -= 1
                    if counter[task]>0:
                        task_list.append((-counter[task], task))
            for t in task_list:
                heapq.heappush(heap, t)
        return res
            