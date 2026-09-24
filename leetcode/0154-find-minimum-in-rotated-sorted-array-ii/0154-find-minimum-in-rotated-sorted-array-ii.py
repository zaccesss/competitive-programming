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

                left = mid + 1

            # minimum is in the left half including mid
            elif nums[mid] < nums[right]:

                right = mid

            # cannot determine side because of duplicates
            # safely shrink search space
            else:
                right -= 1

        # left pointer points to minimum value
        return nums[left]