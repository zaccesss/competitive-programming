from bisect import bisect_right

class Solution:
    def earliestFinishTime(
        self,
        landStartTime: List[int],
        landDuration: List[int],
        waterStartTime: List[int],
        waterDuration: List[int]
    ) -> int:

        def solve(start1, duration1, start2, duration2):

            rides = sorted(zip(start2, duration2))
            starts = [s for s, d in rides]

            m = len(rides)

            # Used prefixMin to store minimum duration.
            prefixMin = [0] * m
            prefixMin[0] = rides[0][1]

            for i in range(1, m):
                prefixMin[i] = min(
                    prefixMin[i - 1],
                    rides[i][1]
                )

            # Used suffixMin to store minimum start+duration.
            suffixMin = [0] * m
            suffixMin[-1] = rides[-1][0] + rides[-1][1]

            for i in range(m - 2, -1, -1):
                suffixMin[i] = min(
                    suffixMin[i + 1],
                    rides[i][0] + rides[i][1]
                )

            answer = float("inf")

            for s, d in zip(start1, duration1):

                # Calculated finish time of first ride.
                finish = s + d

                idx = bisect_right(starts, finish)

                # Used rides already open.
                if idx > 0:
                    answer = min(
                        answer,
                        finish + prefixMin[idx - 1]
                    )

                # Used rides opening later.
                if idx < m:
                    answer = min(
                        answer,
                        suffixMin[idx]
                    )

            return answer

        return min(
            solve(
                landStartTime,
                landDuration,
                waterStartTime,
                waterDuration
            ),
            solve(
                waterStartTime,
                waterDuration,
                landStartTime,
                landDuration
            )
        )