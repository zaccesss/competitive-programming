class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        # dictionary to store the latest index
        # of each number
        seen = {}

        # loop through array with index
        for i, num in enumerate(nums):

            # if number already exists
            if num in seen:

                # check distance between indices
                if i - seen[num] <= k:
                    return True

            # update latest index of number
            seen[num] = i

        # no valid duplicate found
        return False