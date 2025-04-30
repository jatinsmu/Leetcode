"""
https://leetcode.com/problems/merge-intervals/description/
"""
from typing import List


class Solution:

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals = sorted(intervals, key=lambda x: x[0])
        previous_interval = intervals[0]  # initialize with first interval

        counter = 1
        result = [previous_interval]  # a new list where we will add intervals, intitiate with first interval available

        while counter < len(intervals):
            current_interval = intervals[counter]
            # if start of current interval is less than end of prev interval, then merge
            if current_interval[0] <= previous_interval[1]:
                previous_interval[1] = max(current_interval[1], previous_interval[
                    1])  # make the end of prev interval the max of end of current and prev interval. It will be updated in place in result list

            else:
                # current one did not collide with prev interval, so add it as it is
                previous_interval = intervals[counter]
                result.append(previous_interval)

            counter += 1

        return result
