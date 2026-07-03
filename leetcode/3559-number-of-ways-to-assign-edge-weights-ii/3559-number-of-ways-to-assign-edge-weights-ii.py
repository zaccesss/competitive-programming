from collections import deque
from typing import List

class Solution:
    def assignEdgeWeights(
        self,
        edges: List[List[int]],
        queries: List[List[int]]
    ) -> List[int]:

        MOD = 1_000_000_007

        # Used n to store number of nodes.
        n = len(edges) + 1

        # Built adjacency list for the tree.
        graph = [[] for _ in range(n + 1)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        LOG = (n + 1).bit_length()

        # Used depth to store node depths.
        depth = [0] * (n + 1)

        # Used parent to store immediate ancestors.
        parent = [0] * (n + 1)

        # Built depths and parents using BFS.
        q = deque([1])

        while q:

            node = q.popleft()

            for nxt in graph[node]:

                if nxt == parent[node]:
                    continue

                parent[nxt] = node

                depth[nxt] = depth[node] + 1

                q.append(nxt)

        # Used binary lifting table.
        up = [[0] * (n + 1) for _ in range(LOG)]

        up[0] = parent[:]

        # Built binary lifting ancestors.
        for j in range(1, LOG):

            prev = up[j - 1]

            curr = up[j]

            for node in range(1, n + 1):

                curr[node] = prev[prev[node]]

        # Precomputed powers of two modulo MOD.
        pow2 = [1] * n

        for i in range(1, n):

            pow2[i] = (
                pow2[i - 1] * 2
            ) % MOD

        # Used LCA to find lowest common ancestor.
        def lca(a: int, b: int) -> int:

            if depth[a] < depth[b]:

                a, b = b, a

            diff = depth[a] - depth[b]

            bit = 0

            while diff:

                if diff & 1:

                    a = up[bit][a]

                diff >>= 1

                bit += 1

            if a == b:

                return a

            for j in range(LOG - 1, -1, -1):

                if up[j][a] != up[j][b]:

                    a = up[j][a]

                    b = up[j][b]

            return up[0][a]

        # Used answer to store query results.
        answer = [0] * len(queries)

        # Processed all queries.
        for i, (u, v) in enumerate(queries):

            ancestor = lca(u, v)

            # Calculated distance.
            dist = (
                depth[u]
                + depth[v]
                - 2 * depth[ancestor]
            )

            # Empty path has no valid assignments.
            if dist:

                # Answer equals 2^(distance - 1).
                answer[i] = pow2[dist - 1]

        # Returned all query answers.
        return answer