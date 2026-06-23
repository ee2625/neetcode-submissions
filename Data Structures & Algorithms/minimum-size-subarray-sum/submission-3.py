class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        best = float('inf')
        curr = []
        left = 0
        for i in range(len(nums)):
            curr.append(nums[i])
            while sum(curr) >= target:
                best = min(best,len(curr))
                curr.remove(curr[left])


        if best == float('inf'):
            return 0
        else:
            return best