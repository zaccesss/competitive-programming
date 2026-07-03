class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        # Store merged result
        result = []

        # Pointers for both strings
        i = 0
        j = 0

        # Continue while both strings still have characters
        while i < len(word1) and j < len(word2):

            # Add character from word1
            result.append(word1[i])

            # Add character from word2
            result.append(word2[j])

            # Move both pointers forward
            i += 1
            j += 1

        # Add remaining characters from word1
        while i < len(word1):
            result.append(word1[i])
            i += 1

        # Add remaining characters from word2
        while j < len(word2):
            result.append(word2[j])
            j += 1

        # Convert list into string
        return "".join(result)