class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        left = 0
        window_sum = 0
        min_length = float("inf")

        # expand the window
        for right in range(len(nums)):
            window_sum += nums[right]

            # shrink while the current window satisfies the condition
            while window_sum >= target:

                # update the smallest valid window
                min_length = min(min_length, right - left + 1)

                # remove the leftmost element and shrink the window
                window_sum -= nums[left]
                left += 1

        # if no valid subarray exists
        if min_length == float("inf"):
            return 0

        return min_length