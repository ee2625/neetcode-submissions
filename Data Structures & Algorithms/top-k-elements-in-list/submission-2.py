class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        buckets = []

        for num in nums:
            frequency[num] = frequency.get(num,0) + 1

        for i in range(len(nums)+1):
            buckets.append([])

        for num,count in frequency.items():
            buckets[count].append(num)
        
        result = []

        for count in range(len(nums),0,-1):
            for num in buckets[count]:
                result.append(num)
                if len(result) == k:
                    return result
            

