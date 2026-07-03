class Solution:
    def check(self, nums: List[int]) -> bool:

        # Used a counter to track order breaks
        count = 0

        # Looped through the array
        for i in range(len(nums)):

            # Checked if the current number is greater than the next
            if nums[i] > nums[(i + 1) % len(nums)]:
                count += 1

        # Returned True if there is at most one break
        return count <= 1