class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count1 = {}
        for num in nums:
            count1[num] = count1.get(num,0) + 1
            if count1[num] > 1:
                return True
        return False