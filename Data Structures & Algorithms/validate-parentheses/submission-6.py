class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for value in s:
            if value == '{' or value =='(' or value == '[':
                stack.append(value)
            else:
                if not stack:
                    return False
                num = stack.pop()
                if value == '}' and num != '{':
                    return False
                if value == ')' and num != '(':
                    return False
                if value == ']' and num != '[':
                    return False                
        return len(stack) == 0