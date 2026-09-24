class Solution:
    def findMin(self, nums: List[int]) -> int:

        # left and right pointers
        left = 0
        right = len(nums) - 1

        # binary search
        while left < right:

            # middle index
            mid = (left + right) // 2

            # minimum is in the right half
            if nums[mid] > nums[right]:

                # ignore left half including mid
                left = mid + 1

            else:
                # minimum is at mid or in left half
                right = mid

        # left pointer will point to minimum value
        return nums[left]