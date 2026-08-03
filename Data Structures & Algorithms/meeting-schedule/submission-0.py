"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key = lambda x:x.start)
        end = []
        for interval in intervals:
            if end and interval.start < end[-1]:
                return False
            else:
                end.append(interval.end)
        return True