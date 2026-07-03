class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        # Pointer for position of next unique element
        k = 1

        # Start from second element
        for i in range(1, len(nums)):

            # Found a new unique number
            if nums[i] != nums[i - 1]:

                # Place unique number at index k
                nums[k] = nums[i]

                # Move k forward
                k += 1

        # k = number of unique elements
        return k