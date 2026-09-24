class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:

        # used n for length.
        n = len(s)

        # used dp to mark reachable indices.
        dp = [False] * n
        dp[0] = True

        # used count to track reachable positions in window.
        count = 0

        # looped through string.
        for i in range(1, n):

            # added new index entering window.
            if i - minJump >= 0 and dp[i - minJump]:
                count += 1

            # removed index leaving window.
            if i - maxJump - 1 >= 0 and dp[i - maxJump - 1]:
                count -= 1

            # marked reachable if window has valid path and position is '0'.
            dp[i] = count > 0 and s[i] == '0'

        # returned if last index is reachable.
        return dp[n - 1]