class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for x in nums:
            count[x] = count.get(x,0) + 1
        sorted_count = sorted(count.items(), key = lambda x:x[1], reverse= True)
        ans = []
        for i in range(k):
            ans.append(sorted_count[i][0])
        return ans