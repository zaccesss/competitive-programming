class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        left = 0
        window_sum = 0
        min_length = float("inf")

        # Expand the window
        for right in range(len(nums)):
            window_sum += nums[right]

            # Shrink while the current window satisfies the condition
            while window_sum >= target:

                # Update the smallest valid window
                min_length = min(min_length, right - left + 1)

                # Remove the leftmost element and shrink the window
                window_sum -= nums[left]
                left += 1

        # If no valid subarray exists
        if min_length == float("inf"):
            return 0

        return min_length