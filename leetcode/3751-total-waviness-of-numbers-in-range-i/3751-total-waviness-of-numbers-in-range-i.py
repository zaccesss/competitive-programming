class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:

        # used total to store total waviness.
        total = 0

        # processed every number in the range.
        for num in range(num1, num2 + 1):

            # converted number to string.
            s = str(num)

            # skipped numbers with fewer than 3 digits.
            if len(s) < 3:
                continue

            # checked every middle digit.
            for i in range(1, len(s) - 1):

                left = int(s[i - 1])
                curr = int(s[i])
                right = int(s[i + 1])

                # counted peaks.
                if curr > left and curr > right:
                    total += 1

                # counted valleys.
                elif curr < left and curr < right:
                    total += 1

        # returned total waviness.
        return total