class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ans = []
        for val in tokens:
            if val == '+':
                nums1 = ans.pop()
                nums2 = ans.pop()
                ans.append(nums2 + nums1)
            elif val == '-':
                nums1 = ans.pop()
                nums2 = ans.pop()
                ans.append(nums2 - nums1)
            elif val == '*':
                nums1 = ans.pop()
                nums2 = ans.pop()
                ans.append(nums2 * nums1)
            elif val == '/':
                nums1 = ans.pop()
                nums2 = ans.pop()
                ans.append(int(nums2 / nums1))
            else:
                ans.append(int(val))
        return ans[-1]