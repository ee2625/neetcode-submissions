class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        count = {}
        i = 0
        for num in nums:
            if target - num in count:
                return [count[target-num],i]
            else:
                count[num] = i
                i += 1