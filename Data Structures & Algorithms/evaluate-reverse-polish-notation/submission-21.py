class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for val in tokens:
            if val not in '+-*/':
                stack.append(val)
            else:
                num1 = int(stack.pop())
                num2 = int(stack.pop())
                if val == '+':
                    stack.append(num2 + num1)
                elif val == '-':
                    stack.append(num2 - num1)
                elif val == '*':
                    stack.append(num2 * num1)
                elif val == '/':
                    stack.append(int(num2 / num1))
        return int(stack[-1])