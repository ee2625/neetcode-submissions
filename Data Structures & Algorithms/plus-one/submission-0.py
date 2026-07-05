class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = ''
        for value in digits:
            num += str(value)
        num = int(num)
        result = num + 1
        result = str(result)
        ans = []
        for val in result:
            ans.append(int(val))
        return ans
