import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x: x.start)
        ends = []
        for interval in intervals:
            if ends and interval.start >= ends[0]:
                heapq.heappop(ends)
            
            heapq.heappush(ends,interval.end)
        return len(ends)