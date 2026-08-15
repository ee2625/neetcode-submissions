class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        count = 0
        best = float('inf')
        total = 0
        for i in range(len(nums)):
            total += nums[i]
            count += 1
            while left <= i and total >= target:
                best = min(best,count)
                total -= nums[left]
                count -= 1
                left += 1
        if best == float('inf'):
            return 0
        else:
            return best