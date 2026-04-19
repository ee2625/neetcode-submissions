class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        while i < len(nums):
            if target - nums[i] in nums and i != nums.index(target - nums[i]):
                return sorted([i,nums.index(target - nums[i])])
            else:
                i += 1
        