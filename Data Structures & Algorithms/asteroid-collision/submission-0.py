class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for ast in asteroids:
            stack.append(ast)
            while stack and len(stack)>1 and (stack[-1]<0 and stack[-2]>0):
                ast1, ast2 = stack.pop(), stack.pop()
                if abs(ast1)>abs(ast2):
                    stack.append(ast1)
                elif abs(ast1)<abs(ast2):
                    stack.append(ast2)
                else:
                    break
        return stack