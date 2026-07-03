class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # Used two pointers for binary search
        left = 0
        right = len(nums) - 1

        # Looped while the search range is valid
        while left <= right:

            # Calculated the middle index
            mid = (left + right) // 2

            # Returned the index if target was found
            if nums[mid] == target:
                return mid

            # Checked if the left half is sorted
            if nums[left] <= nums[mid]:

                # Searched the left half if target is within range
                if nums[left] <= target < nums[mid]:
                    right = mid - 1

                # Otherwise searched the right half
                else:
                    left = mid + 1

            # Otherwise the right half must be sorted
            else:

                # Searched the right half if target is within range
                if nums[mid] < target <= nums[right]:
                    left = mid + 1

                # Otherwise searched the left half
                else:
                    right = mid - 1

        # Returned -1 if target does not exist
        return -1