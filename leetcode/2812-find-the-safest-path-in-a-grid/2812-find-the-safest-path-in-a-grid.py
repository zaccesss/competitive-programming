from collections import deque
from typing import List


class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:

        n = len(grid)

        # Distance from every cell to its nearest thief
        dist = [[-1] * n for _ in range(n)]

        queue = deque()

        # Add every thief into the queue
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    dist[r][c] = 0
                    queue.append((r, c))

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # Multi-source BFS
        while queue:
            r, c = queue.popleft()

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if (
                    0 <= nr < n
                    and 0 <= nc < n
                    and dist[nr][nc] == -1
                ):
                    dist[nr][nc] = dist[r][c] + 1
                    queue.append((nr, nc))

        # Check if a path exists with safeness >= limit
        def can_reach(limit):

            if dist[0][0] < limit:
                return False

            visited = [[False] * n for _ in range(n)]

            queue = deque([(0, 0)])
            visited[0][0] = True

            while queue:

                r, c = queue.popleft()

                if r == n - 1 and c == n - 1:
                    return True

                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc

                    if (
                        0 <= nr < n
                        and 0 <= nc < n
                        and not visited[nr][nc]
                        and dist[nr][nc] >= limit
                    ):
                        visited[nr][nc] = True
                        queue.append((nr, nc))

            return False

        left = 0
        right = max(max(row) for row in dist)

        answer = 0

        while left <= right:

            mid = (left + right) // 2

            if can_reach(mid):
                answer = mid
                left = mid + 1
            else:
                right = mid - 1

        return answer