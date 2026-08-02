import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key = lambda x:x.start)
        end = []
        for interval in intervals:
            start = interval.start
            ending = interval.end
            if end and start >= end[0]:
                heapq.heappop(end)
                heapq.heappush(end,ending)
            else:
                heapq.heappush(end,ending)
        return len(end)