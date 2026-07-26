class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        # Count how many times each number appears
        for num in nums:
            frequency[num] = frequency.get(num, 0) + 1
        buckets = [] # [[],[5],[6,2]] 5 appears once etc.
        for i in range(len(nums)+1):
            buckets.append([]) # [] appears 1 time [] appears 2 times etc.

        for num, count in frequency.items():
            buckets[count].append(num)
        result = []
        for count in range(len(nums), 0, -1):
            for num in buckets[count]:
                result.append(num)

                if len(result) == k:
                    return result
