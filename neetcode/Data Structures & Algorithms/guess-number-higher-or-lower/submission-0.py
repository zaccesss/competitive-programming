# the guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:

        # used binary search to find the picked number
        left = 1
        right = n

        # looped while the search range is valid
        while left <= right:

            # calculated the middle number
            mid = (left + right) // 2

            # stored the result from the API
            result = guess(mid)

            # returned the number if the guess was correct
            if result == 0:
                return mid

            # searched the left half if the guess was too high
            elif result == -1:
                right = mid - 1

            # otherwise searched the right half
            else:
                left = mid + 1