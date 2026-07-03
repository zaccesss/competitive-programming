class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # Used set to store current window characters.
        charSet = set()

        # Used left pointer for sliding window.
        left = 0

        # Used longest to track maximum length.
        longest = 0

        # Looped through string using right pointer.
        for right in range(len(s)):

            # Removed characters until duplicate was removed.
            while s[right] in charSet:
                charSet.remove(s[left])
                left += 1

            # Added current character to set.
            charSet.add(s[right])

            # Updated longest substring length.
            longest = max(longest, right - left + 1)

        # Returned longest substring length.
        return longest