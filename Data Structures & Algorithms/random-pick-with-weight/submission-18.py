import random
class Solution:
    def __init__(self, w: List[int]):
        self.runningsum = []
        self.total = 0
        for i in range(len(w)):
            self.total += w[i]
            self.runningsum.append(self.total)
    def pickIndex(self) -> int:
        num = random.randint(1,self.total)
        left = 0
        right = len(self.runningsum) - 1
        while left <= right:
            mid = (left + right) // 2
            if num <= self.runningsum[mid]:
                right = mid - 1  
            else:
                left = mid + 1
        return left
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()