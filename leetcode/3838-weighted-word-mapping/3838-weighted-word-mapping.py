class Solution:
    def mapWordWeights(
        self,
        words: List[str],
        weights: List[int]
    ) -> str:

        result = []

        # Processed each word.
        for word in words:

            total = 0

            # Calculated word weight.
            for ch in word:

                total += (
                    weights[
                        ord(ch) - ord('a')
                    ]
                )

            value = total % 26

            # Mapped using reverse alphabet.
            result.append(
                chr(
                    ord('z') - value
                )
            )

        # Returned final string.
        return "".join(result)