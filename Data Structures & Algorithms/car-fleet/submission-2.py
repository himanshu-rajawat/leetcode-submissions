class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_speed = []
        for i in range(len(position)):
            pos_speed.append([position[i], speed[i]])
        pos_speed.sort()

        time_arr = []

        for state in pos_speed:
            pos, spd = state[0], state[1]
            time_arr.append((target-pos)/spd)

        stack = []
        print(time_arr)

        for time in time_arr:
            while stack and stack[-1]<=time:
                stack.pop()
            stack.append(time)
        return len(stack)       #number of remaining time data-> number of fleet

        