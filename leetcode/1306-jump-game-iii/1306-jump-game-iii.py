class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:

        # queue for BFS
        queue = deque([start])

        # track visited indices
        visited = set([start])

        while queue:

            # current index
            i = queue.popleft()

            # found value 0
            if arr[i] == 0:
                return True

            # jump forward
            forward = i + arr[i]

            # jump backward
            backward = i - arr[i]

            # check forward position
            if (
                0 <= forward < len(arr)
                and forward not in visited
            ):

                visited.add(forward)
                queue.append(forward)

            # check backward position
            if (
                0 <= backward < len(arr)
                and backward not in visited
            ):

                visited.add(backward)
                queue.append(backward)

        # no path reaches 0
        return False