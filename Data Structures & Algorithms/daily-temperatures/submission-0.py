class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        days_list = [0]*len(temperatures)

        for i, a in enumerate(temperatures):
            if stack and stack[-1][-2] <a:
                while stack and stack[-1][-2] <a:
                    temp_index = stack.pop()[-1]
                    days_list[temp_index] = i-temp_index
            
            stack.append([a,i])
        return days_list
        