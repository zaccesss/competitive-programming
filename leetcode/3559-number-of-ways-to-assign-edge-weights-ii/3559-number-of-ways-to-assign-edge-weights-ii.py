from collections import deque
from typing import List

class Solution:
    def assignEdgeWeights(
        self,
        edges: List[List[int]],
        queries: List[List[int]]
    ) -> List[int]:

        MOD = 1_000_000_007

        # used n to store number of nodes.
        n = len(edges) + 1

        # built adjacency list for the tree.
        graph = [[] for _ in range(n + 1)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        LOG = (n + 1).bit_length()

        # used depth to store node depths.
        depth = [0] * (n + 1)

        # used parent to store immediate ancestors.
        parent = [0] * (n + 1)

        # built depths and parents using BFS.
        q = deque([1])

        while q:

            node = q.popleft()

            for nxt in graph[node]:

                if nxt == parent[node]:
                    continue

                parent[nxt] = node

                depth[nxt] = depth[node] + 1

                q.append(nxt)

        # used binary lifting table.
        up = [[0] * (n + 1) for _ in range(LOG)]

        up[0] = parent[:]

        # built binary lifting ancestors.
        for j in range(1, LOG):

            prev = up[j - 1]

            curr = up[j]

            for node in range(1, n + 1):

                curr[node] = prev[prev[node]]

        # precomputed powers of two modulo MOD.
        pow2 = [1] * n

        for i in range(1, n):

            pow2[i] = (
                pow2[i - 1] * 2
            ) % MOD

        # used LCA to find lowest common ancestor.
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

        # used answer to store query results.
        answer = [0] * len(queries)

        # processed all queries.
        for i, (u, v) in enumerate(queries):

            ancestor = lca(u, v)

            # calculated distance.
            dist = (
                depth[u]
                + depth[v]
                - 2 * depth[ancestor]
            )

            # empty path has no valid assignments.
            if dist:

                # answer equals 2^(distance - 1).
                answer[i] = pow2[dist - 1]

        # returned all query answers.
        return answer