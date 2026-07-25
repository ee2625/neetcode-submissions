class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for val in s:
            if val in '({[':
                stack.append(val)
            else:
                if not stack:
                    return False
                num = stack.pop()
                if num == '(' and val != ')':
                    return False
                if num == '{' and val != '}':
                    return False
                if num == '[' and val != ']':
                    return False
        return len(stack) == 0