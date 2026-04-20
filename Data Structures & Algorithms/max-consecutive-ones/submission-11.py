class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maximum = 0
        current_streak = 0 
        for i in range(len(nums)):
            if nums[i] == 1:
                current_streak += 1
                maximum = max(maximum,current_streak)
            else:
                current_streak = 0
        return maximum
