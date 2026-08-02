class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1
            while left <=right:
                if nums[i] == nums[left]:
                    return nums[i]
                elif nums[i] == nums[right]:
                    return nums[i]
                elif left < right and nums[left] == nums[right]:
                    return nums[left]
                else:
                    left += 1
                    right -= 1