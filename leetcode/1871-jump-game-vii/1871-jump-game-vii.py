class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:

        # Used n for length.
        n = len(s)

        # Used dp to mark reachable indices.
        dp = [False] * n
        dp[0] = True

        # Used count to track reachable positions in window.
        count = 0

        # Looped through string.
        for i in range(1, n):

            # Added new index entering window.
            if i - minJump >= 0 and dp[i - minJump]:
                count += 1

            # Removed index leaving window.
            if i - maxJump - 1 >= 0 and dp[i - maxJump - 1]:
                count -= 1

            # Marked reachable if window has valid path and position is '0'.
            dp[i] = count > 0 and s[i] == '0'

        # Returned if last index is reachable.
        return dp[n - 1]