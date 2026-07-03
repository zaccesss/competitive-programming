# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:

        # Used binary search to find the picked number
        left = 1
        right = n

        # Looped while the search range is valid
        while left <= right:

            # Calculated the middle number
            mid = (left + right) // 2

            # Stored the result from the API
            result = guess(mid)

            # Returned the number if the guess was correct
            if result == 0:
                return mid

            # Searched the left half if the guess was too high
            elif result == -1:
                right = mid - 1

            # Otherwise searched the right half
            else:
                left = mid + 1