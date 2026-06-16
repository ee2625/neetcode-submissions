class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = {}
        i = 0
        for value in nums:
            if value in seen:
                return True
            else:
                seen[value] = i
                i += 1
        return False