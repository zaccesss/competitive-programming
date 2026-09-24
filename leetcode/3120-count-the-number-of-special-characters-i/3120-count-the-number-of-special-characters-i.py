class Solution:
    def numberOfSpecialChars(self, word: str) -> int:

        # used lowercase set to store lowercase letters.
        lowercase = set()

        # used uppercase set to store uppercase letters.
        uppercase = set()

        # looped through each character in word.
        for char in word:

            # added lowercase characters to lowercase set.
            if char.islower():
                lowercase.add(char)

            # added uppercase characters as lowercase versions.
            else:
                uppercase.add(char.lower())

        # returned count of characters present in both sets.
        return len(lowercase & uppercase)