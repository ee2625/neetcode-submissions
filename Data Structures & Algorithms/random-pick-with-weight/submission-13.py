import random
class Solution:

    def __init__(self, w: List[int]):
        
        self.runningsum = []
        self.total = 0
        for num in w:
            self.total += num
            self.runningsum.append(self.total)


    def pickIndex(self) -> int:
        number = random.randint(1,self.total)
        left = 0
        right = len(self.runningsum) - 1
        while left <= right:
            mid = (left + right) // 2
            if number == self.runningsum[mid]:
                return mid        
            elif number > self.runningsum[mid]:
                left = mid + 1
            else:
                right = mid -1
        return left