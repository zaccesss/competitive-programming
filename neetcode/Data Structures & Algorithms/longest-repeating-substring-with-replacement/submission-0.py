class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        # Used dictionary to store character frequencies.
        count = {}

        # Used left pointer for sliding window.
        left = 0

        # Used maxFreq to store highest character frequency.
        maxFreq = 0

        # Used result to store longest valid window.
        result = 0

        # Looped through string using right pointer.
        for right in range(len(s)):

            # Added current character frequency.
            count[s[right]] = count.get(s[right], 0) + 1

            # Updated highest frequency in current window.
            maxFreq = max(maxFreq, count[s[right]])

            # Shrunk window if replacements needed exceeded k.
            while (right - left + 1) - maxFreq > k:

                # Removed left character from frequency count.
                count[s[left]] -= 1

                # Moved left pointer forward.
                left += 1

            # Updated longest valid substring length.
            result = max(result, right - left + 1)

        # Returned longest repeating character length.
        return result