import random

class Solution:

    def __init__(self, w: List[int]):
        
        self.prefix = []

        runningsum = 0
        for val in w:
            runningsum += val
            self.prefix.append(runningsum)
        
        self.total = runningsum

    def pickIndex(self) -> int:
        left = 0 
        right = len(self.prefix) - 1
        target = random.randint(1,self.total)

        while left <= right:
            mid = (left + right) // 2

            if self.prefix[mid] >= target:
                right = mid - 1
            else:
                left = mid + 1
        return left