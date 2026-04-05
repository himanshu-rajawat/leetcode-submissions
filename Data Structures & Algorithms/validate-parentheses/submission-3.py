class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        para_map = {'{':'}', '[':']', '(':')'}

        for char in s:
            if char in ['{', '(', '[']:
                stack.append(char)
            else:
                if not stack:
                    return False
                ele = stack.pop()

                if ele not in para_map or para_map[ele]!=char:
                    return False
        return len(stack)==0

        