class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        best = 0
        total = 0
        for num in nums:
            if num == 1:
                total += 1
                best = max(best,total)
            else:
                total = 0
        return best