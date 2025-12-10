from typing import List


class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        result = []
        i = 0
        n = len(intervals)

        # Phase 1 - add intervals that come before new interval
        while i < n and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1

        # Phase 2 - merge all overlapping intervals with new interval
        merged_start = newInterval[0]
        merged_end = newInterval[1]

        while i < n and intervals[i][0] <= newInterval[1]:
            merged_start = min(merged_start, intervals[i][0])
            merged_end = max(merged_end, intervals[i][1])
            i += 1

        result.append([merged_start, merged_end])

        # Phase 3 - add all remaining intervals
        while i < n:
            result.append(intervals[i])
            i += 1

        return result
