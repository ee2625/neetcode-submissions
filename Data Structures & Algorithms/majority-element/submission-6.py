class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        for x in nums:
            count[x] = count.get(x,0) + 1
            if count[x] > (len(nums) // 2):
                return x
