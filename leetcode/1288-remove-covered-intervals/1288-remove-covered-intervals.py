class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]):
        # Sort by left ascending, right descending.
        intervals.sort(key=lambda x: (x[0], -x[1]))

        count = 0
        maxRight = 0

        for left, right in intervals:
            # Not covered.
            if right > maxRight:
                count += 1
                maxRight = right

        return count