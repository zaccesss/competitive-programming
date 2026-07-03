from typing import List
import heapq

class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:

        n = len(nums)

        # Used sparse tables for range maximum and minimum queries.
        st_max = [nums[:]]
        st_min = [nums[:]]

        level = 1

        # Built sparse tables.
        while (1 << level) <= n:

            prev_max = st_max[level - 1]
            prev_min = st_min[level - 1]

            size = n - (1 << level) + 1

            cur_max = [0] * size
            cur_min = [0] * size

            half = 1 << (level - 1)

            for i in range(size):

                cur_max[i] = max(
                    prev_max[i],
                    prev_max[i + half]
                )

                cur_min[i] = min(
                    prev_min[i],
                    prev_min[i + half]
                )

            st_max.append(cur_max)
            st_min.append(cur_min)

            level += 1

        # Used RMQ to get subarray value in O(1).
        def value(left: int, right: int) -> int:

            length = right - left + 1
            power = length.bit_length() - 1

            maximum = max(
                st_max[power][left],
                st_max[power][right - (1 << power) + 1]
            )

            minimum = min(
                st_min[power][left],
                st_min[power][right - (1 << power) + 1]
            )

            return maximum - minimum

        # Used max heap to track largest remaining subarray values.
        heap = []

        # Added the largest interval for every starting index.
        for left in range(n):

            heapq.heappush(
                heap,
                (-value(left, n - 1), left, n - 1)
            )

        # Used answer to store the maximum total value.
        answer = 0

        # Processed the k largest distinct subarrays.
        for _ in range(k):

            current_value, left, right = heapq.heappop(heap)

            answer += -current_value

            # Added the next candidate interval.
            if right > left:

                heapq.heappush(
                    heap,
                    (
                        -value(left, right - 1),
                        left,
                        right - 1
                    )
                )

        # Returned the maximum total value.
        return answer