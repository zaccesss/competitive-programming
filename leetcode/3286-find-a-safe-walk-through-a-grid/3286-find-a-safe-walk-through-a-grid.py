from collections import deque
from typing import List


class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:

        m = len(grid)
        n = len(grid[0])

        # dist[r][c] = minimum health lost to reach (r, c)
        dist = [[float("inf")] * n for _ in range(m)]

        # starting cell may already cost 1 health
        dist[0][0] = grid[0][0]

        dq = deque()
        dq.append((0, 0))

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while dq:

            r, c = dq.popleft()

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                if 0 <= nr < m and 0 <= nc < n:

                    # cost to enter the next cell
                    new_cost = dist[r][c] + grid[nr][nc]

                    if new_cost < dist[nr][nc]:
                        dist[nr][nc] = new_cost

                        # safe cell (cost 0): process sooner
                        if grid[nr][nc] == 0:
                            dq.appendleft((nr, nc))
                        else:
                            dq.append((nr, nc))

        # must finish with at least 1 health remaining
        return dist[m - 1][n - 1] < health