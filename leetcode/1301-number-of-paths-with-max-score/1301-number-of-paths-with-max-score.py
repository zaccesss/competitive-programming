class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:

        MOD = 10**9 + 7
        n = len(board)

        # dpScore[r][c] = maximum score from (r, c) to S
        dpScore = [[-1] * n for _ in range(n)]

        # dpWays[r][c] = number of paths that achieve dpScore[r][c]
        dpWays = [[0] * n for _ in range(n)]

        # I started from S with a score of 0 and one valid path.
        dpScore[n - 1][n - 1] = 0
        dpWays[n - 1][n - 1] = 1

        # I processed the board from bottom-right to top-left.
        for row in range(n - 1, -1, -1):
            for col in range(n - 1, -1, -1):

                # I skipped obstacles.
                if board[row][col] == "X":
                    continue

                # I skipped S because I already initialized it.
                if row == n - 1 and col == n - 1:
                    continue

                bestScore = -1
                ways = 0

                # I checked the three possible moves:
                # down, right and down-right.
                for nextRow, nextCol in (
                    (row + 1, col),
                    (row, col + 1),
                    (row + 1, col + 1),
                ):

                    if nextRow >= n or nextCol >= n:
                        continue

                    if dpScore[nextRow][nextCol] == -1:
                        continue

                    # I found a better score.
                    if dpScore[nextRow][nextCol] > bestScore:
                        bestScore = dpScore[nextRow][nextCol]
                        ways = dpWays[nextRow][nextCol]

                    # I found another path with the same best score.
                    elif dpScore[nextRow][nextCol] == bestScore:
                        ways = (ways + dpWays[nextRow][nextCol]) % MOD

                # I skipped cells that cannot reach S.
                if bestScore == -1:
                    continue

                # I added the value of the current cell.
                value = 0
                if board[row][col].isdigit():
                    value = int(board[row][col])

                dpScore[row][col] = bestScore + value
                dpWays[row][col] = ways

        # If E is unreachable, I returned [0, 0].
        if dpWays[0][0] == 0:
            return [0, 0]

        return [dpScore[0][0], dpWays[0][0]]