from collections import deque
from typing import List


class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:

        n = len(online)

        graph = [[] for _ in range(n)]
        indegree = [0] * n

        max_cost = 0

        # Build graph and indegree
        for u, v, w in edges:
            graph[u].append((v, w))
            indegree[v] += 1
            max_cost = max(max_cost, w)

        # Topological order (only once)
        queue = deque()

        for i in range(n):
            if indegree[i] == 0:
                queue.append(i)

        topo = []

        while queue:
            u = queue.popleft()
            topo.append(u)

            for v, _ in graph[u]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    queue.append(v)

        # Check whether score >= limit is possible
        def check(limit):

            INF = float("inf")
            dp = [INF] * n
            dp[0] = 0

            for u in topo:

                if dp[u] == INF:
                    continue

                # Offline intermediate nodes cannot be used
                if u != 0 and u != n - 1 and not online[u]:
                    continue

                for v, w in graph[u]:

                    if w < limit:
                        continue

                    if v != n - 1 and not online[v]:
                        continue

                    dp[v] = min(dp[v], dp[u] + w)

            return dp[n - 1] <= k

        left = 0
        right = max_cost
        answer = -1

        while left <= right:

            mid = (left + right) // 2

            if check(mid):
                answer = mid
                left = mid + 1
            else:
                right = mid - 1

        return answer