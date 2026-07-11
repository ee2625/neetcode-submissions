class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count = {}
        for val in nums:
            count[val] = count.get(val,0) + 1
            if count[val] > 1:
                return True
        return False