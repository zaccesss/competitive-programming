class Solution:
    def isPalindrome(self, s: str) -> bool:

        # pointer at the beginning
        left = 0

        # pointer at the end
        right = len(s) - 1

        while left < right:

            # skip non-alphanumeric characters from the left
            while left < right and not s[left].isalnum():
                left += 1

            # skip non-alphanumeric characters from the right
            while left < right and not s[right].isalnum():
                right -= 1

            # compare characters ignoring case
            if s[left].lower() != s[right].lower():
                return False

            # move both pointers inward
            left += 1
            right -= 1

        return True