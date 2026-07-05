class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ans = []
        for val in tokens:
            if val != '+' and val != '-' and val != '*' and val != '/':
                ans.append(int(val))
            if val == '+':
                add = ans[-1] + ans[-2]
                ans.pop()
                ans.pop()
                ans.append(add)
            elif val == '*':
                add = ans[-1] * ans[-2]
                ans.pop()
                ans.pop()
                ans.append(add)
            elif val == '-':
                add = ans[-2] - ans[-1]
                ans.pop()
                ans.pop()
                ans.append(add)
            elif val == '/':
                add = int(ans[-2] / ans[-1])
                ans.pop()
                ans.pop()
                ans.append(add)
        return ans[-1]
                
