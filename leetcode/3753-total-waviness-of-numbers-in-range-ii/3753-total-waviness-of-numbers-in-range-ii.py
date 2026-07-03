from functools import lru_cache

class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:

        def solve(n: int) -> int:
            if n < 0:
                return 0

            digits = list(map(int, str(n)))
            m = len(digits)

            @lru_cache(None)
            def dp(pos, tight, started, second_last, last):
                if pos == m:
                    # Returned one valid number
                    return (1, 0)

                limit = digits[pos] if tight else 9

                total_count = 0
                total_waviness = 0

                for d in range(limit + 1):
                    next_tight = tight and (d == limit)

                    if not started and d == 0:
                        cnt, wav = dp(
                            pos + 1,
                            next_tight,
                            False,
                            -1,
                            -1
                        )

                        total_count += cnt
                        total_waviness += wav
                        continue

                    if not started:
                        cnt, wav = dp(
                            pos + 1,
                            next_tight,
                            True,
                            -1,
                            d
                        )

                        total_count += cnt
                        total_waviness += wav
                        continue

                    add = 0

                    if second_last != -1:
                        # Added peak check
                        if last > second_last and last > d:
                            add = 1

                        # Added valley check
                        elif last < second_last and last < d:
                            add = 1

                    cnt, wav = dp(
                        pos + 1,
                        next_tight,
                        True,
                        last,
                        d
                    )

                    total_count += cnt

                    # Added waviness contribution
                    total_waviness += wav + cnt * add

                return (total_count, total_waviness)

            return dp(0, True, False, -1, -1)[1]

        # Returned answer for range
        return solve(num2) - solve(num1 - 1)