import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x: x.start)
        ends = []
        for interval in intervals:
            # Reuse the room that becomes available first
            if ends and interval.start >= ends[0]:
                heapq.heappop(ends)

            # Assign the current meeting to a room
            heapq.heappush(ends, interval.end)

        return len(ends)