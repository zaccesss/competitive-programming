class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        # Pointer at the start of the array
        left = 0

        # Pointer at the end of the array
        right = len(s) - 1

        # Keep swapping until pointers meet
        while left < right:

            # Swap characters at left and right positions
            s[left], s[right] = s[right], s[left]

            # Move left pointer forward
            left += 1

            # Move right pointer backward
            right -= 1