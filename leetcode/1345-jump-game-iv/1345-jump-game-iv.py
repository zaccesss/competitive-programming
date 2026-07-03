class Solution:
    def minJumps(self, arr: List[int]) -> int:

        n = len(arr)

        # Already at last index
        if n == 1:
            return 0

        # Store indices for each value
        graph = defaultdict(list)

        for i, num in enumerate(arr):
            graph[num].append(i)

        # BFS queue: (index, steps)
        queue = deque([(0, 0)])

        # Track visited indices
        visited = set([0])

        while queue:

            index, steps = queue.popleft()

            # Reached last index
            if index == n - 1:
                return steps

            # All possible next positions
            neighbors = graph[arr[index]]

            # Add adjacent indices
            neighbors.append(index - 1)
            neighbors.append(index + 1)

            for nxt in neighbors:

                # Valid unvisited index
                if 0 <= nxt < n and nxt not in visited:

                    visited.add(nxt)
                    queue.append((nxt, steps + 1))

            # Clear list to avoid revisiting
            # same-value indices again
            graph[arr[index]].clear()