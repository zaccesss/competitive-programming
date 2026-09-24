class Solution:
    def rotate(self, nums: List[int], k: int) -> None:

        # used modulo to handle large k values.
        k %= len(nums)

        # used helper to reverse a range in-place.
        def reverse(left, right):

            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        # reversed the entire array.
        reverse(0, len(nums) - 1)

        # reversed the first k elements.
        reverse(0, k - 1)

        # reversed the remaining elements.
        reverse(k, len(nums) - 1)