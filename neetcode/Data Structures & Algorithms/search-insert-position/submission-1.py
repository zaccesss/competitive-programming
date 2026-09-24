class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

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

            # searched the right half if target is larger
            elif nums[mid] < target:
                left = mid + 1

            # otherwise searched the left half
            else:
                right = mid - 1

        # returned the position where target should be inserted
        return left