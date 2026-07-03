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

                # Ignore left half including mid
                left = mid + 1

            else:
                # Minimum is at mid or in left half
                right = mid

        # Left pointer will point to minimum value
        return nums[left]