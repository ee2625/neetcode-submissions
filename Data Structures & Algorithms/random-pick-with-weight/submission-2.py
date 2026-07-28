import random

class Solution:

    def __init__(self, w: List[int]):
        self.prefix = []

        running_sum = 0

        for weight in w:
            running_sum += weight
            self.prefix.append(running_sum)

        self.total = running_sum

    def pickIndex(self) -> int:
        target = random.randint(1, self.total)

        left = 0
        right = len(self.prefix) - 1

        while left < right:
            middle = (left + right) // 2

            if self.prefix[middle] >= target:
                right = middle
            else:
                left = middle + 1

        return left