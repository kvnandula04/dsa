from typing import List


class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:

        if not intervals:
            return [newInterval]

        new_start = newInterval[0]
        new_end = newInterval[1]

        output = []
        overlap = []
        new_interval_added = False  # Add this flag

        for interval in intervals:
            start = interval[0]
            end = interval[1]

            # If new interval already added, just append remaining intervals
            if new_interval_added:
                output.append(interval)
                continue

            # interval completely before new interval
            if end < new_start:
                output.append(interval)

            # interval completely after new interval
            elif start > new_end:
                if overlap:
                    output.append(
                        [min(overlap[0][0], new_start), max(overlap[-1][1], new_end)]
                    )
                else:
                    output.append([new_start, new_end])

                new_interval_added = True
                output.append(interval)
                overlap = []

            # overlap
            else:
                overlap.append(interval)

        if overlap:
            output.append([min(overlap[0][0], new_start), max(overlap[-1][1], new_end)])
        elif not new_interval_added:  # Add this condition
            output.append([new_start, new_end])

        return output


sol = Solution()

print(sol.insert([[1, 5]], [6, 8]))
print(sol.insert([[1, 3], [6, 9]], [2, 5]))
print(sol.insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]))
print(sol.insert([[2, 5], [6, 7], [8, 9]], [0, 1]))
