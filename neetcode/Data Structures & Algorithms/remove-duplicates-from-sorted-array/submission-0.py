class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        # pointer for position of next unique element
        k = 1

        # start from second element
        for i in range(1, len(nums)):

            # found a new unique number
            if nums[i] != nums[i - 1]:

                # place unique number at index k
                nums[k] = nums[i]

                # move k forward
                k += 1

        # k = number of unique elements
        return k