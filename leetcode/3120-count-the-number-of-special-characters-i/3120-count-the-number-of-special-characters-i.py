class Solution:
    def numberOfSpecialChars(self, word: str) -> int:

        # Used lowercase set to store lowercase letters.
        lowercase = set()

        # Used uppercase set to store uppercase letters.
        uppercase = set()

        # Looped through each character in word.
        for char in word:

            # Added lowercase characters to lowercase set.
            if char.islower():
                lowercase.add(char)

            # Added uppercase characters as lowercase versions.
            else:
                uppercase.add(char.lower())

        # Returned count of characters present in both sets.
        return len(lowercase & uppercase)