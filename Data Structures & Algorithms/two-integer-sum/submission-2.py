class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        i = 0
        for value in nums:

            if target - value in seen:
                # found what I need
                return [seen[target-value],i]

            seen[value] = i
            i += 1
        