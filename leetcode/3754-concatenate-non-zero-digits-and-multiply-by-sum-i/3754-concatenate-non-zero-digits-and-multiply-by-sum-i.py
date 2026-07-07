class Solution:
    def sumAndMultiply(self, n: int) -> int:

        # built the number using only the non-zero digits
        digits = []

        # kept only the non-zero digits
        for ch in str(n):
            if ch != "0":
                digits.append(ch)

        # If there were no non-zero digits, x = 0
        if not digits:
            return 0

        # formed x by concatenating the remaining digits
        x = int("".join(digits))

        # calculated the sum of the digits in x
        digitSum = 0
        for ch in digits:
            digitSum += int(ch)

        # I returned x multiplied by its digit sum
        return x * digitSum