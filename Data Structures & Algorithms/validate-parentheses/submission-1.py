class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        look_up_dict = {'(':')','[':']','{':'}'}

        for char in s:
            if char in ['(','[','{']:
                stack.append(char)
            else:
                last_ele = stack.pop() if len(stack)>0 else None
                if not last_ele or look_up_dict[last_ele]!=char:
                    return False
        return True if len(stack)==0 else False

        