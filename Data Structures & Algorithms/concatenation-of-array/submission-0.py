class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        output = nums.copy()
        for i in nums:
            output.append(i)
        return output