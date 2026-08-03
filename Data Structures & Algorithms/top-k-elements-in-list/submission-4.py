import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        frequency = {}

        for val in nums:
            frequency[val] = frequency.get(val,0) + 1
        
        buckets= []
        for i in range(len(nums)+1):
            buckets.append([])
        
        for num, count in frequency.items():
            buckets[count].append(num)
        ans = []
        for i in range(len(nums),0,-1):
            for val in buckets[i]:
                ans.append(val)
                if len(ans) == k:
                    return ans