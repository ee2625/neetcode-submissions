import random
class Solution:
    def __init__(self, w: List[int]):
        self.runningtotal = []
        self.total = 0
        for i in range(len(w)):
            self.total += w[i]
            self.runningtotal.append(self.total)
    def pickIndex(self) -> int:
        num = random.randint(1,self.total)
        left = 0
        right = len(self.runningtotal) - 1
        while left <= right:
            mid = (left + right) // 2
            if self.runningtotal[mid] >= num:
                right = mid - 1
            else:
                left = mid + 1

        return mid
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()