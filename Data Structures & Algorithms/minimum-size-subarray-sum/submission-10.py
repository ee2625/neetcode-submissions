class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        count = 0
        total = 0
        best = float('inf')
        for i in range(len(nums)):
            total += nums[i]
            count += 1
            while total >= target:
                best = min(best,count)
                total -= nums[left]
                left += 1
                count -= 1
        if  best == float('inf'):
            return 0
        else:
            return best