class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:

        # used two pointers for both arrays
        i = 0
        j = 0

        # looped through both arrays
        while i < len(nums1) and j < len(nums2):

            # returned the value if both numbers match
            if nums1[i] == nums2[j]:
                return nums1[i]

            # moved i forward if nums1 has the smaller number
            elif nums1[i] < nums2[j]:
                i += 1

            # otherwise moved j forward
            else:
                j += 1

        # returned -1 if no common value exists
        return -1