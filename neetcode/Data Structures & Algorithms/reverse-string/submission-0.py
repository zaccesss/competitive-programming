class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        # pointer at the start of the array
        left = 0

        # pointer at the end of the array
        right = len(s) - 1

        # keep swapping until pointers meet
        while left < right:

            # swap characters at left and right positions
            s[left], s[right] = s[right], s[left]

            # move left pointer forward
            left += 1

            # move right pointer backward
            right -= 1