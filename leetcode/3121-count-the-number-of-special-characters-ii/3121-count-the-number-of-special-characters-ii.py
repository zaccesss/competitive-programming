class Solution:
    def numberOfSpecialChars(self, word: str) -> int:

        # used dictionary to store last lowercase positions.
        lastLower = {}

        # used dictionary to store first uppercase positions.
        firstUpper = {}

        # looped through each character with index.
        for i, char in enumerate(word):

            # stored last position of lowercase character.
            if char.islower():
                lastLower[char] = i

            # stored first position of uppercase character.
            else:
                lowerChar = char.lower()

                if lowerChar not in firstUpper:
                    firstUpper[lowerChar] = i

        # used count to track special characters.
        count = 0

        # looped through lowercase characters.
        for char in lastLower:

            # checked if character existed in uppercase.
            if char in firstUpper:

                # checked if all lowercase came before uppercase.
                if lastLower[char] < firstUpper[char]:
                    count += 1

        # returned total special characters.
        return count