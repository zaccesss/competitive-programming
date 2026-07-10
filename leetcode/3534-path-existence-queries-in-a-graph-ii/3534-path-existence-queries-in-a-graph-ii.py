from typing import List

class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:

        # sorted the nodes by their values
        order = sorted(range(n), key=lambda i: nums[i])

        # stored each node's position in the sorted order
        pos = [0] * n
        for i, node in enumerate(order):
            pos[node] = i

        # built the next reachable index
        nxt = [0] * n

        j = 0
        for i in range(n):
            while j + 1 < n and nums[order[j + 1]] - nums[order[i]] <= maxDiff:
                j += 1
            nxt[i] = j

        LOG = n.bit_length()

        # built the binary lifting table
        up = [n - 1] * (LOG + 1)
        up = [[n - 1] * n for _ in range(LOG)]

        for i in range(n):
            up[0][i] = nxt[i]

        for k in range(1, LOG):
            for i in range(n):
                up[k][i] = up[k - 1][up[k - 1][i]]

        answer = []

        # answered each query
        for u, v in queries:

            left = pos[u]
            right = pos[v]

            if left > right:
                left, right = right, left

            # already at the same node
            if left == right:
                answer.append(0)
                continue

            # impossible to reach
            if nxt[left] == left:
                answer.append(-1)
                continue

            jumps = 0
            cur = left

            # binary lifted as far as possible without passing right
            for k in range(LOG - 1, -1, -1):
                if up[k][cur] < right:
                    cur = up[k][cur]
                    jumps += 1 << k

            # checked whether one more jump reaches the target
            if nxt[cur] >= right:
                answer.append(jumps + 1)
            else:
                answer.append(-1)

        return answer