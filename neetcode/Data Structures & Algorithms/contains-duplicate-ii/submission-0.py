class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        # Dictionary to store the latest index
        # of each number
        seen = {}

        # Loop through array with index
        for i, num in enumerate(nums):

            # If number already exists
            if num in seen:

                # Check distance between indices
                if i - seen[num] <= k:
                    return True

            # Update latest index of number
            seen[num] = i

        # No valid duplicate found
        return False