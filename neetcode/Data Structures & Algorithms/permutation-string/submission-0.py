class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        # Returned false if s1 was longer than s2.
        if len(s1) > len(s2):
            return False

        # Used count1 to store frequencies of s1.
        count1 = [0] * 26

        # Used count2 to store frequencies of current window.
        count2 = [0] * 26

        # Added frequencies for s1 and first window.
        for i in range(len(s1)):
            count1[ord(s1[i]) - ord('a')] += 1
            count2[ord(s2[i]) - ord('a')] += 1

        # Returned true if first window matched.
        if count1 == count2:
            return True

        # Looped through remaining characters in s2.
        for right in range(len(s1), len(s2)):

            # Added new character entering window.
            count2[ord(s2[right]) - ord('a')] += 1

            # Removed character leaving window.
            count2[ord(s2[right - len(s1)]) - ord('a')] -= 1

            # Returned true if frequencies matched.
            if count1 == count2:
                return True

        # Returned false if no permutation was found.
        return False