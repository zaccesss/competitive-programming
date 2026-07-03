class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:

        # Used two pointers for both arrays
        i = 0
        j = 0

        # Looped through both arrays
        while i < len(nums1) and j < len(nums2):

            # Returned the value if both numbers match
            if nums1[i] == nums2[j]:
                return nums1[i]

            # Moved i forward if nums1 has the smaller number
            elif nums1[i] < nums2[j]:
                i += 1

            # Otherwise moved j forward
            else:
                j += 1

        # Returned -1 if no common value exists
        return -1