import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key = lambda x:x.start)
        
        if len(intervals) == 0 or len(intervals) == 1:
            return len(intervals)
        ends = [intervals[0].end]
        for i in range(1,len(intervals)):
            start = intervals[i].start
            end = intervals[i].end
            if start < ends[0]:
                heapq.heappush(ends,end)
            else:
                heapq.heappop(ends)
                heapq.heappush(ends,end)
        return len(ends)