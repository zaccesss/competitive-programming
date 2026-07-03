class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        # Used result to store valid triplets.
        result = []

        # Sorted array for two pointer approach.
        nums.sort()

        # Looped through array using index i.
        for i in range(len(nums)):

            # Skipped duplicate values for i.
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Used left pointer after i.
            left = i + 1

            # Used right pointer at end of array.
            right = len(nums) - 1

            # Looped while left pointer was smaller than right.
            while left < right:

                # Calculated current triplet sum.
                total = nums[i] + nums[left] + nums[right]

                # Moved left pointer if sum was too small.
                if total < 0:
                    left += 1

                # Moved right pointer if sum was too large.
                elif total > 0:
                    right -= 1

                # Added valid triplet if sum equalled zero.
                else:
                    result.append([nums[i], nums[left], nums[right]])

                    # Moved left pointer forward.
                    left += 1

                    # Moved right pointer backward.
                    right -= 1

                    # Skipped duplicate left values.
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

        # Returned all unique triplets.
        return result   