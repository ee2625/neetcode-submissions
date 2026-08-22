class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        left = 0 
        count = 1
        best = 1
        for i in range(1,len(nums)):
            if nums[i] - nums[left] == 1:
                count += 1
                left = i
                best = max(best,count)
            if nums[i] - nums[i- 1] > 1:
                left = i
                count = 1
        return best