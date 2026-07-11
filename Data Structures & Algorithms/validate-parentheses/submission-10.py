class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for val in s:
            if val in '([{':
                stack.append(val)
            else:
                if len(stack) == 0:
                    return False
                num = stack.pop()
                if val == ')' and num != '(':
                    return False
                if val == ']' and num != '[':
                    return False
                if val == '}' and num != '{':
                    return False

        return len(stack) == 0