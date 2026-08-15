import heapq
class MedianFinder:

    def __init__(self):
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small,-num)

        value = -self.small[0]
        heapq.heappush(self.large,value)
        heapq.heappop(self.small)

        if len(self.large) > len(self.small):
            value = -heapq.heappop(self.large)
            heapq.heappush(self.small,value)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -self.small[0]
        return (-self.small[0] + self.large[0]) / 2
        
        