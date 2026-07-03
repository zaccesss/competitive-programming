class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:

        # Used memoization to store already calculated results
        memo = {}

        # Created DFS to find the maximum jumps from an index
        def dfs(i):

            # Returned stored result if already calculated
            if i in memo:
                return memo[i]

            # Started with 1 because the current index counts
            max_jump = 1

            # Checked jumps to the left
            for j in range(i - 1, max(-1, i - d - 1), -1):

                # Stopped if a larger or equal value blocks the path
                if arr[j] >= arr[i]:
                    break

                # Updated the maximum path length
                max_jump = max(max_jump, 1 + dfs(j))

            # Checked jumps to the right
            for j in range(i + 1, min(len(arr), i + d + 1)):

                # Stopped if a larger or equal value blocks the path
                if arr[j] >= arr[i]:
                    break

                # Updated the maximum path length
                max_jump = max(max_jump, 1 + dfs(j))

            # Stored the calculated result
            memo[i] = max_jump

            return max_jump

        # Returned the largest path from all starting positions
        return max(dfs(i) for i in range(len(arr)))