class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        best = float('inf')
        while left <= right:
            mid = (right + left) // 2
            best = min(best,nums[mid])
            if nums[left] < nums[mid]:
                if nums[right] < nums[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                if nums[left] > nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
        return best