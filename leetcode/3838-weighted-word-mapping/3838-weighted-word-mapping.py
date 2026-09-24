class Solution:
    def mapWordWeights(
        self,
        words: List[str],
        weights: List[int]
    ) -> str:

        result = []

        # processed each word.
        for word in words:

            total = 0

            # calculated word weight.
            for ch in word:

                total += (
                    weights[
                        ord(ch) - ord('a')
                    ]
                )

            value = total % 26

            # mapped using reverse alphabet.
            result.append(
                chr(
                    ord('z') - value
                )
            )

        # returned final string.
        return "".join(result)