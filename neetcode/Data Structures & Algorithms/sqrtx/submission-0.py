class Solution:
    def mySqrt(self, x: int) -> int:

        # used binary search to find the square root
        left = 0
        right = x

        # looped while the search range is valid
        while left <= right:

            # calculated the middle number
            mid = (left + right) // 2

            # calculated the square of mid
            square = mid * mid

            # returned the result if a perfect square was found
            if square == x:
                return mid

            # searched the right half if square is smaller
            elif square < x:
                left = mid + 1

            # otherwise searched the left half
            else:
                right = mid - 1

        # returned the rounded down square root
        return right