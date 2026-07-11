class Solution:
    def isValid(self, s: str) -> bool:
        ans = []
        for val in s:
            if val in '({[':
                ans.append(val)
            else:
                if len(ans) == 0:
                    return False
                num = ans.pop()
                if val == ')' and num != '(':
                    return False
                if val == ']' and num != '[':
                    return False           
                if val == '}' and num != '{':
                    return False
        return len(ans) == 0

