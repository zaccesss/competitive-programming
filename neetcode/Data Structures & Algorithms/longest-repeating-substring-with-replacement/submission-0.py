class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        # used dictionary to store character frequencies.
        count = {}

        # used left pointer for sliding window.
        left = 0

        # used maxFreq to store highest character frequency.
        maxFreq = 0

        # used result to store longest valid window.
        result = 0

        # looped through string using right pointer.
        for right in range(len(s)):

            # added current character frequency.
            count[s[right]] = count.get(s[right], 0) + 1

            # updated highest frequency in current window.
            maxFreq = max(maxFreq, count[s[right]])

            # shrunk window if replacements needed exceeded k.
            while (right - left + 1) - maxFreq > k:

                # removed left character from frequency count.
                count[s[left]] -= 1

                # moved left pointer forward.
                left += 1

            # updated longest valid substring length.
            result = max(result, right - left + 1)

        # returned longest repeating character length.
        return result