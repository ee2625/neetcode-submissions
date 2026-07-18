class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        best = float('inf')
        while left <= right:
            mid = (left + right) // 2
            if nums[left] <= nums[mid]: # left is sorted
                best = min(best,nums[left])
                left = mid + 1
            else: # right is sorted
                best = min(best,nums[mid])
                right = mid - 1
        return best
