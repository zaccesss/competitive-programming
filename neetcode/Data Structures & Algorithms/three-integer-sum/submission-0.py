class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        # used result to store valid triplets.
        result = []

        # sorted array for two pointer approach.
        nums.sort()

        # looped through array using index i.
        for i in range(len(nums)):

            # skipped duplicate values for i.
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # used left pointer after i.
            left = i + 1

            # used right pointer at end of array.
            right = len(nums) - 1

            # looped while left pointer was smaller than right.
            while left < right:

                # calculated current triplet sum.
                total = nums[i] + nums[left] + nums[right]

                # moved left pointer if sum was too small.
                if total < 0:
                    left += 1

                # moved right pointer if sum was too large.
                elif total > 0:
                    right -= 1

                # added valid triplet if sum equalled zero.
                else:
                    result.append([nums[i], nums[left], nums[right]])

                    # moved left pointer forward.
                    left += 1

                    # moved right pointer backward.
                    right -= 1

                    # skipped duplicate left values.
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

        # returned all unique triplets.
        return result   