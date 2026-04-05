class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # first sort the position from lower to higher and also combine speed with it, now start from first pair of position and speed and keep appending to a stack if last entry will not reach new entry
        def will_form_fleet(curr_pos, curr_speed, last_pos, last_speed):
            return last_speed>curr_speed and ((target-curr_pos)/curr_speed)>=((curr_pos-last_pos)/(last_speed-curr_speed))
        stack = []
        for i in range(len(position)):
            position[i] = [position[i], speed[i]]
        position.sort()

        for data in position:
            pos, spd = data[0], data[1]

            while stack and will_form_fleet(pos, spd, stack[-1][0], stack[-1][1]):
                stack.pop()
            stack.append(data)
        
        return len(stack)

        