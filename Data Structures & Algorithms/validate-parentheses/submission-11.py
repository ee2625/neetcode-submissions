class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for val in s:
            if val in "{([":
                stack.append(val)
            else:
                if not stack:
                    return False
                num = stack.pop()
                if val == "}" and num != "{":
                    return False
                if val == ")" and num != "(":
                    return False
                if val == "]" and num != "[":
                    return False
        return len(stack) == 0