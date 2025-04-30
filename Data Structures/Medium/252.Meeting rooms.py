"""
https://leetcode.com/problems/meeting-rooms/description/
"""
from typing import List

"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""


class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # sort all meetings according to start times
        if len(intervals) > 0:
            intervals = sorted(intervals, key=lambda x: x.start)
            previous_interval = intervals[0]  # initialize first interval as previous

            counter = 1
            while counter < len(intervals):
                current_interval = intervals[counter]
                # check if end time of previous is less than start time of current
                if previous_interval.end <= current_interval.start:
                    # true, this can be done. Make previous as current and move on the next interval
                    previous_interval = current_interval
                else:
                    return False

                counter += 1

        # if we reach this point, then all are possible
        return True
