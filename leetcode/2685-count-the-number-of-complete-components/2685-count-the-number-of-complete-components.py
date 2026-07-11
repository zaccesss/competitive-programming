class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:

        # built the adjacency list
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # tracked the visited nodes
        visited = [False] * n

        answer = 0

        # performed dfs on each component
        for start in range(n):

            if visited[start]:
                continue

            stack = [start]
            visited[start] = True

            nodes = 0
            degreeSum = 0

            # explored the current component
            while stack:

                node = stack.pop()

                nodes += 1
                degreeSum += len(graph[node])

                for neighbor in graph[node]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        stack.append(neighbor)

            # counted the edges in the component
            edgesInComponent = degreeSum // 2

            # checked whether the component is complete
            if edgesInComponent == nodes * (nodes - 1) // 2:
                answer += 1

        return answer