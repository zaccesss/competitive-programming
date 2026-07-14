class Solution:
    def findMin(self, nums: List[int]) -> int:

        left = 0
        right = len(nums) - 1

        # array is already sorted
        if nums[left] <= nums[right]:
            return nums[left]

        while left < right:

            mid = (left + right) // 2

            # minimum is in the right half
            if nums[mid] > nums[right]:
                left = mid + 1

            # minimum is in the left half including mid
            else:
                right = mid

        return nums[left]