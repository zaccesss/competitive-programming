class Solution:
    def rotate(self, nums: List[int], k: int) -> None:

        # Used modulo to handle large k values.
        k %= len(nums)

        # Used helper to reverse a range in-place.
        def reverse(left, right):

            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        # Reversed the entire array.
        reverse(0, len(nums) - 1)

        # Reversed the first k elements.
        reverse(0, k - 1)

        # Reversed the remaining elements.
        reverse(k, len(nums) - 1)