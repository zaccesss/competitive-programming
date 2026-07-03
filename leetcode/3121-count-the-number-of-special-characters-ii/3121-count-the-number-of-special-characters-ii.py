class Solution:
    def numberOfSpecialChars(self, word: str) -> int:

        # Used dictionary to store last lowercase positions.
        lastLower = {}

        # Used dictionary to store first uppercase positions.
        firstUpper = {}

        # Looped through each character with index.
        for i, char in enumerate(word):

            # Stored last position of lowercase character.
            if char.islower():
                lastLower[char] = i

            # Stored first position of uppercase character.
            else:
                lowerChar = char.lower()

                if lowerChar not in firstUpper:
                    firstUpper[lowerChar] = i

        # Used count to track special characters.
        count = 0

        # Looped through lowercase characters.
        for char in lastLower:

            # Checked if character existed in uppercase.
            if char in firstUpper:

                # Checked if all lowercase came before uppercase.
                if lastLower[char] < firstUpper[char]:
                    count += 1

        # Returned total special characters.
        return count