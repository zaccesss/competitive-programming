from collections import defaultdict


class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:

        # Build adjacency list
        graph = defaultdict(list)

        for u, v, w in roads:
            graph[u].append((v, w))
            graph[v].append((u, w))

        visited = set()
        answer = float("inf")

        def dfs(node):
            nonlocal answer

            visited.add(node)

            for neighbor, weight in graph[node]:

                # Update the minimum edge seen
                answer = min(answer, weight)

                if neighbor not in visited:
                    dfs(neighbor)

        dfs(1)

        return answer