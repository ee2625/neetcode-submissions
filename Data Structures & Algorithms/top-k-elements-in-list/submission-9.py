import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        frequency = {}
        for x in nums:
            frequency[x] = frequency.get(x,0) + 1
        
        buckets = []
        for i in range(len(nums)+1):
            buckets.append([])
        
        for val,count in frequency.items():
            buckets[count].append(val)
        ans = []
        for i in range(len(nums),0,-1):
            for num in buckets[i]:
                ans.append(num)
                if len(ans) == k:
                    return ans