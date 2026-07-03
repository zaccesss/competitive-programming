class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:

        # Queue for BFS
        queue = deque([start])

        # Track visited indices
        visited = set([start])

        while queue:

            # Current index
            i = queue.popleft()

            # Found value 0
            if arr[i] == 0:
                return True

            # Jump forward
            forward = i + arr[i]

            # Jump backward
            backward = i - arr[i]

            # Check forward position
            if (
                0 <= forward < len(arr)
                and forward not in visited
            ):

                visited.add(forward)
                queue.append(forward)

            # Check backward position
            if (
                0 <= backward < len(arr)
                and backward not in visited
            ):

                visited.add(backward)
                queue.append(backward)

        # No path reaches 0
        return False