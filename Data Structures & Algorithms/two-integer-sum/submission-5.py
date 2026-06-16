class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        i = 0
        for value in nums:
            if target - value in seen:
                return [seen[target - value],i]
            else:
                seen[value] = i
                i += 1
        