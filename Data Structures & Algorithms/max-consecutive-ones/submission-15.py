class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxi = 0
        curr = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                maxi = max(maxi,curr)
                curr = 0
            else:
                curr += 1

        return max(maxi,curr)