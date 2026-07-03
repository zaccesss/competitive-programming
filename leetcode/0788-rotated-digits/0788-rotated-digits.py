class Solution:
    def rotatedDigits(self, n: int) -> int:
        # Rotating 3, 4 or 7 by 180 degrees does not produce a valid digit.
        # If a number contains any of these, it is invalid -- skip it.
        invalid = {3, 4, 7}

        # These digits rotate into a DIFFERENT valid digit:
        # 2 becomes 5, 5 becomes 2, 6 becomes 9, 9 becomes 6.
        # A number is only "good" if it contains at least one of these,
        # because the rotated result must be different from the original.
        different = {2, 5, 6, 9}

        count = 0

        for x in range(1, n + 1):
            # Split the number into individual digits to check each one.
            digits = [int(d) for d in str(x)]

            # If any digit is invalid, rotating this number breaks it -- skip it.
            if any(d in invalid for d in digits):
                continue

            # Digits 0, 1 and 8 rotate to themselves, so a number made of only
            # those would rotate into an identical number -- that is not "good".
            # Only count this number if at least one digit actually changes.
            if any(d in different for d in digits):
                count += 1

        return count