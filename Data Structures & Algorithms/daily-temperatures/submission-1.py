class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]*len(temperatures)
        stack = []    #every ele in stack will be of form -> [index, temp]

        for i in range(len(temperatures)):
            temp = temperatures[i]
            while stack and stack[-1][1]<temp:
                last_ele = stack.pop()
                last_idx, temp_last = last_ele[0], last_ele[1]
                res[last_idx]= i-last_idx
            stack.append([i,temp])
        return res
        