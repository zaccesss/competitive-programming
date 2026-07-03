class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        # Pointer for last valid element in nums1
        p1 = m - 1

        # Pointer for last element in nums2
        p2 = n - 1

        # Pointer for last position in nums1
        p = m + n - 1

        # Merge from the back
        while p1 >= 0 and p2 >= 0:

            # Place larger value at the end
            if nums1[p1] > nums2[p2]:

                nums1[p] = nums1[p1]

                # Move nums1 pointer left
                p1 -= 1

            else:

                nums1[p] = nums2[p2]

                # Move nums2 pointer left
                p2 -= 1

            # Move final position pointer left
            p -= 1

        # If nums2 still has remaining elements
        # copy them into nums1
        while p2 >= 0:

            nums1[p] = nums2[p2]

            p2 -= 1
            p -= 1
        