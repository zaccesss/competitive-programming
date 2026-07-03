class Solution:
    def findMin(self, nums: List[int]) -> int:

        # Left and right pointers
        left = 0
        right = len(nums) - 1

        # Binary search
        while left < right:

            # Middle index
            mid = (left + right) // 2

            # Minimum is in the right half
            if nums[mid] > nums[right]:

                left = mid + 1

            # Minimum is in the left half including mid
            elif nums[mid] < nums[right]:

                right = mid

            # Cannot determine side because of duplicates
            # Safely shrink search space
            else:
                right -= 1

        # Left pointer points to minimum value
        return nums[left]