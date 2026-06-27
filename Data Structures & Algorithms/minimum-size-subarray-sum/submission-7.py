class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        count = 0
        best = float('inf')
        for i in range(len(nums)):
            count += nums[i]
            if count >= target:
                while count >= target:
                    best = min(best,i - left + 1)
                    count -= nums[left]
                    left += 1
        if best == float('inf'):
            return 0
        else:
            return best