class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        best = nums[0]

        while left <= right:
            if nums[left] <= nums[right]:
                best = min(best, nums[left])
                break

            mid = (left + right) // 2
            best = min(best, nums[mid])

            if nums[mid] >= nums[left]:
                left = mid + 1
            else:
                right = mid - 1

        return best