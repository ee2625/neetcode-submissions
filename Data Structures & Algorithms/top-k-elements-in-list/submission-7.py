class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        frequency = {}
        buckets = []
        for i in range(len(nums)+1):
            buckets.append([])
        
        for i in range(len(nums)):
            frequency[nums[i]] = frequency.get(nums[i],0) + 1
        
        for num, count in frequency.items():
            buckets[count].append(num)
        ans = []
        for i in range(len(nums),0,-1):
            for num in buckets[i]:
                ans.append(num)
                if len(ans) == k:
                    return ans
