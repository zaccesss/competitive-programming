class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        # store merged result
        result = []

        # pointers for both strings
        i = 0
        j = 0

        # continue while both strings still have characters
        while i < len(word1) and j < len(word2):

            # add character from word1
            result.append(word1[i])

            # add character from word2
            result.append(word2[j])

            # move both pointers forward
            i += 1
            j += 1

        # add remaining characters from word1
        while i < len(word1):
            result.append(word1[i])
            i += 1

        # add remaining characters from word2
        while j < len(word2):
            result.append(word2[j])
            j += 1

        # convert list into string
        return "".join(result)