class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:

        result = []
        digits = "123456789"

        lowLength = len(str(low))
        highLength = len(str(high))

        for length in range(lowLength, highLength + 1):

            for start in range(10 - length):

                number = int(digits[start:start + length])

                if low <= number <= high:
                    result.append(number)

        return result