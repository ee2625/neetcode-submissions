class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count1 = {}
        for value in nums:
            if value in count1:
                count1[value] += 1
                if count1[value] > (len(nums) // 2):
                    return value
            else:
                count1[value] = 1
        return nums[0]