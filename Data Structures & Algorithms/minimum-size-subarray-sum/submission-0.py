class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        best = float('inf')
        curr = 0
        for i in range(len(nums)):
            curr += nums[i]
            while curr >= target:
                best = min(best,i - left + 1)
                curr -= nums[left]
                left += 1
        if best == float('inf'):
            return 0
        else:
            return best