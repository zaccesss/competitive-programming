class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:

        # Used total to store total waviness.
        total = 0

        # Processed every number in the range.
        for num in range(num1, num2 + 1):

            # Converted number to string.
            s = str(num)

            # Skipped numbers with fewer than 3 digits.
            if len(s) < 3:
                continue

            # Checked every middle digit.
            for i in range(1, len(s) - 1):

                left = int(s[i - 1])
                curr = int(s[i])
                right = int(s[i + 1])

                # Counted peaks.
                if curr > left and curr > right:
                    total += 1

                # Counted valleys.
                elif curr < left and curr < right:
                    total += 1

        # Returned total waviness.
        return total