class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        for value in nums:
            count[value] = count.get(value,0) + 1
            if count[value] > (len(nums) // 2):
                return value
        