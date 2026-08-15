class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key = lambda x:x.start)
        if len(intervals) == 0 or len(intervals) == 1:
            return True
        for i in range(1,len(intervals)):
            end = intervals[i-1].end
            start = intervals[i].start
            if start < end:
                return False
        return True
