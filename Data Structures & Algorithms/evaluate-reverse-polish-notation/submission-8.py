class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ans = []
        for val in tokens:
            if val == '+':
                num1 = ans.pop()
                num2 = ans.pop()
                ans.append(num1 + num2)
            elif val == '*':
                num1 = ans.pop()
                num2 = ans.pop()
                ans.append(num1 * num2)
            elif val == '-':
                num1 = ans.pop()
                num2 = ans.pop()
                ans.append(num2 - num1)
            elif val == '/':
                num1 = ans.pop()
                num2 = ans.pop()
                ans.append(int(num2 / num1))
            else:
                ans.append(int(val))
        return ans[-1]
