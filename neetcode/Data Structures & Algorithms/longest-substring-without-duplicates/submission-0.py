class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # used set to store current window characters.
        charSet = set()

        # used left pointer for sliding window.
        left = 0

        # used longest to track maximum length.
        longest = 0

        # looped through string using right pointer.
        for right in range(len(s)):

            # removed characters until duplicate was removed.
            while s[right] in charSet:
                charSet.remove(s[left])
                left += 1

            # added current character to set.
            charSet.add(s[right])

            # updated longest substring length.
            longest = max(longest, right - left + 1)

        # returned longest substring length.
        return longest