class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        best = float('inf')
        total = 0
        left = 0
        for i in range(len(nums)):
            total += nums[i]
            while total >= target:
                best = min(best,i-left + 1)
                total -= nums[left]
                left += 1
        if best == float('inf'):
            return 0
        else:
            return best