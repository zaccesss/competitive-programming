class Solution:
    def validPalindrome(self, s: str) -> bool:

        # Helper function to check if substring is palindrome
        def is_palindrome(left, right):

            while left < right:

                if s[left] != s[right]:
                    return False

                left += 1
                right -= 1

            return True

        # Two pointers
        left = 0
        right = len(s) - 1

        while left < right:

            # If characters do not match
            if s[left] != s[right]:

                # Try skipping either left or right character
                return (
                    is_palindrome(left + 1, right)
                    or
                    is_palindrome(left, right - 1)
                )

            # Move inward
            left += 1
            right -= 1

        return True