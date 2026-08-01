import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key = lambda x:x.start)
        end = []
        for interval in intervals:
            if end and interval.start >= end[0]:
                heapq.heappop(end)


            heapq.heappush(end, interval.end)
        return len(end)