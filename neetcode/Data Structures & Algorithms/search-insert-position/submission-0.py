class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

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

            # Searched the right half if target is larger
            elif nums[mid] < target:
                left = mid + 1

            # Otherwise searched the left half
            else:
                right = mid - 1

        # Returned the position where target should be inserted
        return left