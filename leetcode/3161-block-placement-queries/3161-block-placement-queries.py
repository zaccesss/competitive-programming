from sortedcontainers import SortedList

class SegmentTree:

    def __init__(self, n):

        # used n to store tree size.
        self.n = n

        # used tree to store maximum gap values.
        self.tree = [0] * (4 * n)

    def update(self, node, left, right, idx, value):

        # updated value when leaf node was reached.
        if left == right:
            self.tree[node] = value
            return

        # calculated middle position.
        mid = (left + right) // 2

        # updated left child if index was in left half.
        if idx <= mid:
            self.update(node * 2, left, mid, idx, value)

        # updated right child if index was in right half.
        else:
            self.update(node * 2 + 1, mid + 1, right, idx, value)

        # updated current node maximum value.
        self.tree[node] = max(
            self.tree[node * 2],
            self.tree[node * 2 + 1]
        )

    def query(self, node, left, right, ql, qr):

        # returned zero if range did not overlap.
        if qr < left or right < ql:
            return 0

        # returned node value if range was fully covered.
        if ql <= left and right <= qr:
            return self.tree[node]

        # calculated middle position.
        mid = (left + right) // 2

        # returned maximum value from both halves.
        return max(
            self.query(node * 2, left, mid, ql, qr),
            self.query(node * 2 + 1, mid + 1, right, ql, qr)
        )


class Solution:
    def getResults(self, queries):

        # used maxX to find largest coordinate.
        maxX = 0

        # looped through queries to find maximum x value.
        for q in queries:
            maxX = max(maxX, q[1])

        # used obstacles to store obstacle positions in sorted order.
        obstacles = SortedList([0, maxX + 1])

        # used segment tree to store maximum gap lengths.
        seg = SegmentTree(maxX + 2)

        # stored initial gap from 0 to maxX + 1.
        seg.update(1, 0, maxX + 1, maxX + 1, maxX + 1)

        # used answer to store query results.
        answer = []

        # looped through all queries.
        for q in queries:

            # processed obstacle insertion query.
            if q[0] == 1:

                # used x for obstacle position.
                x = q[1]

                # found insertion position.
                pos = obstacles.bisect_left(x)

                # found neighbouring obstacles.
                right = obstacles[pos]
                left = obstacles[pos - 1]

                # added obstacle to sorted set.
                obstacles.add(x)

                # updated gap ending at new obstacle.
                seg.update(
                    1,
                    0,
                    maxX + 1,
                    x,
                    x - left
                )

                # updated gap ending at right obstacle.
                seg.update(
                    1,
                    0,
                    maxX + 1,
                    right,
                    right - x
                )

            # processed block placement query.
            else:

                # used x for query boundary.
                x = q[1]

                # used size for required block length.
                size = q[2]

                # found last obstacle before or at x.
                pos = obstacles.bisect_right(x)

                # stored nearest obstacle on the left.
                prevObstacle = obstacles[pos - 1]

                # queried largest completed gap before x.
                largestGap = seg.query(
                    1,
                    0,
                    maxX + 1,
                    0,
                    prevObstacle
                )

                # considered partial gap ending at x.
                largestGap = max(
                    largestGap,
                    x - prevObstacle
                )

                # stored whether block could fit.
                answer.append(largestGap >= size)

        # returned all query results.
        return answer