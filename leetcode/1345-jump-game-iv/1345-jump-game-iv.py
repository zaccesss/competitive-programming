class Solution:
    def minJumps(self, arr: List[int]) -> int:

        n = len(arr)

        # already at last index
        if n == 1:
            return 0

        # store indices for each value
        graph = defaultdict(list)

        for i, num in enumerate(arr):
            graph[num].append(i)

        # BFS queue: (index, steps)
        queue = deque([(0, 0)])

        # track visited indices
        visited = set([0])

        while queue:

            index, steps = queue.popleft()

            # reached last index
            if index == n - 1:
                return steps

            # all possible next positions
            neighbors = graph[arr[index]]

            # add adjacent indices
            neighbors.append(index - 1)
            neighbors.append(index + 1)

            for nxt in neighbors:

                # valid unvisited index
                if 0 <= nxt < n and nxt not in visited:

                    visited.add(nxt)
                    queue.append((nxt, steps + 1))

            # clear list to avoid revisiting
            # same-value indices again
            graph[arr[index]].clear()