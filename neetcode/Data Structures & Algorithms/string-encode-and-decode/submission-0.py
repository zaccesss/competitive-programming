class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            # To decode later, you need to know where each string starts and ends.
            # The length of the string is stored before it, separated by "#".
            # For example: ["hello", "world"] becomes "5#hello5#world"
            # When decoding, you read the number, skip the "#", then read that many characters.
            result += str(len(s)) + "#" + s
        return result

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0  # i is the current reading position, starting at the beginning

        while i < len(s):
            j = i

            # Move j forward until the "#" character is found.
            # Everything between i and j is the length number stored during encoding.
            while s[j] != "#":
                j += 1

            # Convert those characters (before "#") into an actual integer.
            # This tells you how many characters the next string contains.
            length = int(s[i:j])

            # Start reading one position after "#", for exactly 'length' characters.
            # That recovers the original string.
            word = s[j + 1 : j + 1 + length]
            result.append(word)

            # Move i to the start of the next encoded entry and repeat.
            i = j + 1 + length

        return result