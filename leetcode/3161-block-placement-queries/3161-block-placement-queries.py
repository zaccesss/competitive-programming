from sortedcontainers import SortedList

class SegmentTree:

    def __init__(self, n):

        # Used n to store tree size.
        self.n = n

        # Used tree to store maximum gap values.
        self.tree = [0] * (4 * n)

    def update(self, node, left, right, idx, value):

        # Updated value when leaf node was reached.
        if left == right:
            self.tree[node] = value
            return

        # Calculated middle position.
        mid = (left + right) // 2

        # Updated left child if index was in left half.
        if idx <= mid:
            self.update(node * 2, left, mid, idx, value)

        # Updated right child if index was in right half.
        else:
            self.update(node * 2 + 1, mid + 1, right, idx, value)

        # Updated current node maximum value.
        self.tree[node] = max(
            self.tree[node * 2],
            self.tree[node * 2 + 1]
        )

    def query(self, node, left, right, ql, qr):

        # Returned zero if range did not overlap.
        if qr < left or right < ql:
            return 0

        # Returned node value if range was fully covered.
        if ql <= left and right <= qr:
            return self.tree[node]

        # Calculated middle position.
        mid = (left + right) // 2

        # Returned maximum value from both halves.
        return max(
            self.query(node * 2, left, mid, ql, qr),
            self.query(node * 2 + 1, mid + 1, right, ql, qr)
        )


class Solution:
    def getResults(self, queries):

        # Used maxX to find largest coordinate.
        maxX = 0

        # Looped through queries to find maximum x value.
        for q in queries:
            maxX = max(maxX, q[1])

        # Used obstacles to store obstacle positions in sorted order.
        obstacles = SortedList([0, maxX + 1])

        # Used segment tree to store maximum gap lengths.
        seg = SegmentTree(maxX + 2)

        # Stored initial gap from 0 to maxX + 1.
        seg.update(1, 0, maxX + 1, maxX + 1, maxX + 1)

        # Used answer to store query results.
        answer = []

        # Looped through all queries.
        for q in queries:

            # Processed obstacle insertion query.
            if q[0] == 1:

                # Used x for obstacle position.
                x = q[1]

                # Found insertion position.
                pos = obstacles.bisect_left(x)

                # Found neighbouring obstacles.
                right = obstacles[pos]
                left = obstacles[pos - 1]

                # Added obstacle to sorted set.
                obstacles.add(x)

                # Updated gap ending at new obstacle.
                seg.update(
                    1,
                    0,
                    maxX + 1,
                    x,
                    x - left
                )

                # Updated gap ending at right obstacle.
                seg.update(
                    1,
                    0,
                    maxX + 1,
                    right,
                    right - x
                )

            # Processed block placement query.
            else:

                # Used x for query boundary.
                x = q[1]

                # Used size for required block length.
                size = q[2]

                # Found last obstacle before or at x.
                pos = obstacles.bisect_right(x)

                # Stored nearest obstacle on the left.
                prevObstacle = obstacles[pos - 1]

                # Queried largest completed gap before x.
                largestGap = seg.query(
                    1,
                    0,
                    maxX + 1,
                    0,
                    prevObstacle
                )

                # Considered partial gap ending at x.
                largestGap = max(
                    largestGap,
                    x - prevObstacle
                )

                # Stored whether block could fit.
                answer.append(largestGap >= size)

        # Returned all query results.
        return answer