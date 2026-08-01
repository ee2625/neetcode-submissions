class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        zeros = 0
        best = 0
        left = 0
        ans = []
        for i in range(len(nums)):
            ans.append(nums[i])
            if nums[i] == 0:
                zeros += 1
            while zeros > k:
                ans.remove(nums[left])
                if nums[left] == 0:
                    zeros -= 1
                left += 1
            
            best = max(best,i - left + 1)
        return best
