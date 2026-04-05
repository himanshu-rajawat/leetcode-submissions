class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ['+', '-', '*', '/']

        def perform_operation(num1, num2, operation):
            if operation == '+':
                return num1+num2
            elif operation == '-':
                return num1-num2
            elif operation == '*':
                return num1*num2
            else:
                return num1/num2

        for token in tokens:
            if token not in operators:
                stack.append(token)
            else:
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(perform_operation(int(num1), int(num2), token))
        return int(stack[0])