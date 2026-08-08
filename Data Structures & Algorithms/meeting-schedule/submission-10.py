class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key = lambda x:x.start)

        for i in range(1,len(intervals)):
            start = intervals[i].start
            end = intervals[i].end
            if start < intervals[i-1].end:
                return False
        return True