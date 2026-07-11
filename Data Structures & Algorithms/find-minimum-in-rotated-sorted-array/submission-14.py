class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        best = max(nums)
        while left <= right:
            mid = (left + right) // 2
            best = min(best,nums[mid])
            if nums[left] <= nums[mid]: # left sorted
                if nums[left] <= nums[right]:
                    right = mid - 1
                else:
                    left = mid + 1
            else: # right sorted
                if nums[left] <= nums[right]:
                    left = mid + 1
                else:
                    right = mid -1
            

        return best