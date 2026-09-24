class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:

        # used memoization to store already calculated results
        memo = {}

        # created DFS to find the maximum jumps from an index
        def dfs(i):

            # returned stored result if already calculated
            if i in memo:
                return memo[i]

            # started with 1 because the current index counts
            max_jump = 1

            # checked jumps to the left
            for j in range(i - 1, max(-1, i - d - 1), -1):

                # stopped if a larger or equal value blocks the path
                if arr[j] >= arr[i]:
                    break

                # updated the maximum path length
                max_jump = max(max_jump, 1 + dfs(j))

            # checked jumps to the right
            for j in range(i + 1, min(len(arr), i + d + 1)):

                # stopped if a larger or equal value blocks the path
                if arr[j] >= arr[i]:
                    break

                # updated the maximum path length
                max_jump = max(max_jump, 1 + dfs(j))

            # stored the calculated result
            memo[i] = max_jump

            return max_jump

        # returned the largest path from all starting positions
        return max(dfs(i) for i in range(len(arr)))