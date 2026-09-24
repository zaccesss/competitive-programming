class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # used two pointers for binary search
        left = 0
        right = len(nums) - 1

        # looped while the search range is valid
        while left <= right:

            # calculated the middle index
            mid = (left + right) // 2

            # returned the index if target was found
            if nums[mid] == target:
                return mid

            # checked if the left half is sorted
            if nums[left] <= nums[mid]:

                # searched the left half if target is within range
                if nums[left] <= target < nums[mid]:
                    right = mid - 1

                # otherwise searched the right half
                else:
                    left = mid + 1

            # otherwise the right half must be sorted
            else:

                # searched the right half if target is within range
                if nums[mid] < target <= nums[right]:
                    left = mid + 1

                # otherwise searched the left half
                else:
                    right = mid - 1

        # returned -1 if target does not exist
        return -1