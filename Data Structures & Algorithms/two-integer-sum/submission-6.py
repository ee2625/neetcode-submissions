class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        group = {}
        ans = []
        i = 0
        for value in nums:
            if target - value in group:
                return [group[target-value],i]
            else:
                group[value] = i
                i += 1
        return ans
        