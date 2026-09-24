class Solution:
    def validPalindrome(self, s: str) -> bool:

        # helper function to check if substring is palindrome
        def is_palindrome(left, right):

            while left < right:

                if s[left] != s[right]:
                    return False

                left += 1
                right -= 1

            return True

        # two pointers
        left = 0
        right = len(s) - 1

        while left < right:

            # if characters do not match
            if s[left] != s[right]:

                # try skipping either left or right character
                return (
                    is_palindrome(left + 1, right)
                    or
                    is_palindrome(left, right - 1)
                )

            # move inward
            left += 1
            right -= 1

        return True