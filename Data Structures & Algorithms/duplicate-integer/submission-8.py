class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        group = {}
        i = 0
        for value in nums:
            if value in group:
                return True
            else:
                group[value] = i
                i +=0 
        return False
